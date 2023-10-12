def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_pokemon', methods=['POST'])
def get_pokemon():
    pokemon_name = request.form.get('pokemon_name')
    data = get_pokemon_data(pokemon_name)
    if data:
        name = data['name']
        image_url = data['sprites']['front_default']
        abilities = [ability['ability']['name'] for ability in data['abilities']]
        return render_template('index.html', name=name, image_url=image_url, abilities=abilities)
    else:
        return "Pokemon not found."

if __name__ == '__main__':
    app.run(debug=True)