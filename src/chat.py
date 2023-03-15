import openai
import json

def initialize():
    print("Welcome to ChatGPTwo, your own personalized Artificial Intelligence.");
    bot = 'src/config.json';
    with open(bot) as f:
        config = json.load(f);
        if(config['foundation']['apikey'] == ""):
            openaikey = input("Please enter your OpenAI API key: ");
            with open(bot, 'w') as f:
                config['foundation']['apikey'] = openaikey;
                json.dump(config, f, indent=4);
    openaikey = config['foundation']['apikey'];
    check();

def check():
    bot = 'src/bots.json';
    with open(bot) as f:
        ai = json.load(f);
        if(ai['1'][0] == "name" and ai['2'][0] == "name" and ai['3'][0] == "name"):
            print("You have not created any A.I.s yet.");
            yn = input("Would you like to create one now? (y / n): ");
            if(yn == "y"):
                creator();
            else:
                print("Goodbye!");
        elif(ai['1'][0] != "name" or ai['2'][0] != "name" or ai['3'][0] != "name"): 
            selector = input("Would you like to create a new A.I. or chat with an existing one? (chat / create): ");
            if(selector == "chat"):
                print("These are the A.I.s you have created:"); 
                for i in range(1, 4):
                    if(ai[str(i)][0] == "name"):
                        continue;
                    else:
                        print("Slot " + str(i) + ": " + ai[str(i)][0]);
                ai = input("Which A.I. would you like to chat with? [1, 2, or 3]: ");
                while(ai != "1" and ai != "2" and ai != "3"):
                    ai = input("Please enter a valid slot number; 1, 2, or 3: ");
                chat(ai);
            elif(selector == "create"):
                creator();
    
def creator():
    bot = 'src/bots.json';
    with open(bot) as f:
        ai = json.load(f);
        print("Lets get started by creating your personalized A.I.");
        name = input("What would you like to name your A.I.?: ");
        while(name == "name"):
            name = input("The name of your A.I. cannot be called 'name'. Please enter a different name: ");
        occupation = input("Where does " + name + " do?: " )
        age = input("How old is " + name + "?: ")
        print("Currently, " + name + " is a " + age + " year old." + occupation + ".");
        personality = input("What is their personality like?: ");
        for i in range(1, 4):
            if(ai[str(i)][0] == "name"):
                print("Slot " + str(i) + ": EMPTY");
            else:
                print("Slot " + str(i) + ": " + ai[str(i)][0]);
        slot = input("Which slot would you like to place " + name + " in?: ");
        while(slot != "1" and slot != "2" and slot != "3"):
            slot = input("Please enter a valid slot number; 1, 2, or 3: ");
        
        with open(bot, 'w') as f: 
            ai[slot][0] = name;
            ai[slot][1] = occupation;
            ai[slot][2] = age;
            ai[slot][3] = personality;    
            json.dump(ai, f, indent=4);
        
        check();
                
def chat(ai):
    traits = ["name", "occupation", "age", "personality"];
    openai.api_key = "";
    
    with open('src/config.json') as f:
        api = json.load(f);
        openai.api_key = api['foundation']['apikey'];
        f.close();
        
    with open('src/bots.json') as f:
        bot = json.load(f);
        for i in range(0,4):
            traits[i] = bot[ai][i];
        f.close();
        
    print("You are currently chatting with " + traits[0] + ".")
        
    while(True):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Your name is " 
                    + traits[0] + ". Respond as a " + traits[2] 
                    + " year old who, " + traits[1] 
                    + " and " + traits[3] +". Do not ask the user questions."},
                {"role": "user", "content": init()}
                
            ]
        )
        print(traits[0] + ": " + response['choices'][0]['message']['content']);

def init():
    prompt = input("You: ");
    return prompt;
    
initialize()