from flask import Flask, request, jsonify
import pandas as pd
import numpy as np

# Initialisation de l'application Flask
app = Flask(__name__)

# Charger les fichiers nécessaires
df = pd.read_excel('./test_calcul_indice_cow_5_crypte.xlsx')
transition_matrix = pd.read_excel('./transition_matrix_formatted_decile_rounded_2.xlsx', index_col=0)

# Ajouter une colonne SCC_Group pour catégoriser SCC en Low, Medium, High
bins = [0, 150, 400, float('inf')]
labels = ['Low', 'Medium', 'High']
df['SCC_Group'] = pd.cut(df['SCC'], bins=bins, labels=labels)

# Route principale pour éviter les erreurs 404
@app.route('/')
def home():
    return "Bienvenue sur l'API Flask de WALLeSmart. Les routes API commencent par '/api/'."

# API pour récupérer les alertes
@app.route('/api/alerts', methods=['GET'])
def get_alerts():
    id_ferme = request.args.get('id_ferme')
    if not id_ferme:
        return jsonify({'error': 'ID_FERME est requis'}), 400

    # Filtrer les données par ferme
    filtered_df = df[df['ID_FERME'] == int(id_ferme)]

    # Calculer les alertes
    alerts = []
    for _, row in filtered_df.iterrows():
        current_group = row['SCC_Group']
        parity = row['Parité']
        if parity in transition_matrix.index:
            transition_probs = transition_matrix.loc[parity]
            prob_to_high = transition_probs.get('High', 0)
            if current_group != 'High' and prob_to_high > 0.5:
                alerts.append({
                    'animal_id': row['ID_ANIMAL'],
                    'probability': round(prob_to_high, 2)
                })

    return jsonify(alerts)

# API pour récupérer les données d'un animal
@app.route('/api/animal_data/<int:id_animal>/<int:id_ferme>', methods=['GET'])
def get_animal_data(id_animal, id_ferme):
    filtered_df = df[(df['ID_ANIMAL'] == id_animal) & (df['ID_FERME'] == id_ferme)]
    if filtered_df.empty:
        return jsonify({'error': 'Aucune donnée trouvée pour cet animal et cette ferme'}), 404

    # Extraire les données de performance
    animal_data = filtered_df[['PNM_LAIT', 'PNM_MG', 'PNM_PROT', 'PNM_SCC']].iloc[0].tolist()
    return jsonify({
        'animal_data': animal_data,
        'labels': ['PNM_LAIT', 'PNM_MG', 'PNM_PROT', 'PNM_SCC']
    })

# API pour personnaliser l'analyse
@app.route('/api/customize_analysis', methods=['POST'])
def customize_analysis():
    data = request.get_json()
    id_ferme = data.get('id_ferme')
    parameters = data.get('parameters', [])

    if not id_ferme:
        return jsonify({'error': 'ID_FERME est requis'}), 400
    if not parameters:
        return jsonify({'error': 'Aucun paramètre sélectionné'}), 400

    # Filtrer les données par ferme
    filtered_df = df[df['ID_FERME'] == int(id_ferme)]
    if filtered_df.empty:
        return jsonify({'error': 'Aucune donnée trouvée pour cette ferme'}), 404

    # Filtrer les colonnes en fonction des paramètres
    selected_columns = []
    if 'cheese_making' in parameters:
        selected_columns += ['CheeseYieldCurd', 'CheeseYieldSolid']
    if 'minerals' in parameters:
        selected_columns += ['Na..mg.kg.', 'Ca..mg.kg.', 'P..mg.kg.', 'Mg..mg.kg.', 'K..mg.kg.']
    if 'energy_balance' in parameters:
        selected_columns += ['milk_bhb_svm', 'DMI_kg_d', 'N_efficiency']
    if 'infections' in parameters:
        selected_columns += ['Natural_Log_SCC', 'milk_nagase_svm', 'Lactoferrin_20170518']
    if 'methane_production' in parameters:
        selected_columns += ['CH4..g.day..532']

    if not selected_columns:
        return jsonify({'error': 'Aucune colonne sélectionnée pour l’analyse'}), 400

    # Préparer les données standardisées
    standardized_data = {}
    for col in selected_columns:
        if col in filtered_df.columns:
            col_mean = filtered_df[col].mean()
            col_std = filtered_df[col].std() or 1  # Éviter une division par zéro
            standardized_data[col] = ((filtered_df[col] - col_mean) / col_std).tolist()

    return jsonify({'standardized_data': standardized_data})

# API pour récupérer les données des top 10 CL max et min
@app.route('/api/top10_cl', methods=['GET'])
def get_top10_cl():
    id_ferme = request.args.get('id_ferme')
    if not id_ferme:
        return jsonify({'error': 'ID_FERME est requis'}), 400

    # Filtrer les données par ferme
    filtered_df = df[df['ID_FERME'] == int(id_ferme)]
    if filtered_df.empty:
        return jsonify({'error': 'Aucune donnée trouvée pour cette ferme'}), 404

    # Calculer les valeurs de CL
    filtered_df['CL'] = filtered_df[['PNM_LAIT', 'PNM_MG', 'PNM_PROT', 'PNM_SCC']].sum(axis=1)

    # Obtenir les top 10 CL max et min
    top10_cl_max = filtered_df.nlargest(10, 'CL')[['ID_ANIMAL', 'CL']].to_dict(orient='records')
    top10_cl_min = filtered_df.nsmallest(10, 'CL')[['ID_ANIMAL', 'CL']].to_dict(orient='records')

    return jsonify({'top10_cl_max': top10_cl_max, 'top10_cl_min': top10_cl_min})

# Lancer l'application Flask
if __name__ == '__main__':
    app.run(debug=True)
