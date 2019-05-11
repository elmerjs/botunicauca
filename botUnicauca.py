#ASISTENTE VIRTUAL UNICAUCA
from chatterbot import ChatBot #se importa la librería del chatbot
from chatterbot import comparisons, response_selection #importamos la libreria de tipo ode comparación y respuesta

chatbot = ChatBot(
    "Experto_unicauca", 

    storage_adapter='chatterbot.storage.MongoDatabaseAdapter', 
    database_uri='mongodb://localhost:27017/chatterbot_unicauca', #utilizamos una base de datos, en este caso mongodb para guardar la documentación de preguntas frecuentes
    input_adapter="chatterbot.input.TerminalAdapter", #formato de entrada del bot
    output_adapter="chatterbot.output.OutputAdapter",#formato de salida del bot
    output_format="text",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch", #tipo de respuesta del bot, lo que encuentre más razonable 
            "statement_comparison_function": comparisons.levenshtein_distance,
            "response_selection_method": response_selection.get_most_frequent_response
        },
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Disculpa, no te he entendido bien,  solo soy experto en Unicauca  Puedes ser más específico',
            'maximum_similarity_threshold': 0.50 #si no cumple con esta medida de reconocimeinto nos dara una respuesta por defecto
        },
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter', #respuesta a una pregunta específica.
            'input_text': 'Quiero saber acerca de Unicauca',
            'output_text': 'Puedes saber acerca de unicauca ahora en: http://portal.unicauca.edu.co/versionP/node/18445'
        },
    ],
    
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace' #limpia los espacios entre letras
    ],
    
    read_only=True, #por ahora no se dejará que aprenda, para efectos de prueba.
)
DEFAULT_SESSION_ID = chatbot.default_session.id
from chatterbot.trainers import ChatterBotCorpusTrainer

trainer = ChatterBotCorpusTrainer(chatbot) #entrenamiento del bot
trainer.train("./univp_ES.yml") # tomamos una base de datos que contiene la información  de la U

while(True): # mientras se hagan pregutnas 
    input_string2 = input('Tu: ') #inicia la conversación ingresando la pregutna el usuario
    response = chatbot.get_response(input_string2) #se captura la respuesta del bot.
    print('Chatbot: '+ response.text) #se muestra en pantalla la respuesta.

#edad = int(input("¿Cuántos años tiene? "))
#if input_string2 = "chao":
#    1|'"
#    )
#else:
#    print("Es usted mayor de edad")
#print("¡Hasta la próxima!")