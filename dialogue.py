from util import key_pressed
import util
from time import sleep

frame_1 = '''
                  ;~~,__
   :-....,-------'`-'._.'
    `-,,,  ,       ,'~~'
        ; ,'~.__; /--.
        :| :|   :|``(;
        `-'`-'  `-''
        loading.
        '''

frame_2 = '''
                  ;~~,__
   :-....,-------'`-'._.'
    `-,,,  ,       ;'~~'
       ,'_,'~.__; '--.
      //'       ````(;
     `-'
        loading..
     '''

frame_3 = '''
                .--~~,__
   :-....,-------`~~'._.'
    `-,,,  ,_      ;'~U'
     _,-' ,'`-__; '--.
    (_/'~~      ''''(;''' + '''
          
        loading...
        '''

element_1 = '''


    .-------------.       .    .   *       *   
    /_/_/_/_/_/_/_/ \         *       .   )    .
  //_/_/_/_/_/_// _ \ __          .        .   
  /_/_/_/_/_/_/_/|/ \.' .`-o                    
  |             ||-'(/ ,--'                    
  |             ||  _ |                        
  |             ||'' ||                        
  |_____________|| |_|L                    

              loading.
'''

element_2 = '''
                                      *
                              *
    .-------------.       .    .   *       *   
    /_/_/_/_/_/_/_/ \         *       .   )    .
  //_/_/_/_/_/_// _ \ __          .        .   
  /_/_/_/_/_/_/_/|/ \.' .`-o           *         .
  |             ||-'(/ ,--'                    
  |             ||  _ |                        
  |             ||'' ||                        
  |_____________|| |_|L                    

              loading..
'''


element_3 = '''


    .-------------.       .    . *     *   
    /_/_/_/_/_/_/_/ \       *       .     )    .
  //_/_/_/_/_/_// _ \ __        .      .   .   *
  /_/_/_/_/_/_/_/|/ \.' .`-o                 .   
  |             ||-'(/ ,--'             *       
  |             ||  _ |                        
  |             ||'' ||                        
  |_____________|| |_|L                    

              loading...
'''

cat_frame_1 = '''
      |\      _,,,---,,_
      /,`.-'`'    -.  ;-;;,_
    |,4-  ) )-,_..;\ (  `'-'
    '---''(_/--'  `-'\_)

        loading.
'''

cat_frame_2 = '''
      |\      _,,,,--,,_
      /,`.-'`'    -,  ;-;,
    |,4-  ) ),,__ ) /;  ;;
    '---''(.'--'  (.'`.) `'

        loading..
'''

cat_frame_3 = '''
      |\      _,,,,--,,_
      /,`.-'`'    -,  \-;,
    |,4-  ) ),,__ ,\ (  ;;
    '---''(.'--'  `-'`.)`'

        loading...
'''

cat_frame_4 = '''
      |\      _,,,--,,_  ,)
      /,`.-'`'   -,  ;-;;'
    |,4-  ) )-,_ ) /\\
    '---''(_/--' (_/-'

        loading....
'''

cat_frames = [cat_frame_1, cat_frame_2, cat_frame_3, cat_frame_4]

frames = [frame_1, frame_2, frame_3]

frames_2 = [element_1, element_2, element_3]

def waiting_screen(frames):
  util.clear_screen()
  range = 0
  while range <10:
    for frame in frames:
      print(frame)
      sleep(0.5)
      util.clear_screen()
      range += 1


def dialogue_with_Benek(player):
    print('''
         ,--._______,-.
       ,','  ,    .  ,_`-.
      / /  ,' , _` ``. |  )       `-..
     (,';'""`/ '"`-._ ` \/ ______    \\
       : ,o.-`- ,o.  )\` -'      `---.))
       : , d8b ^-.   '|   `.      `    `.
       |/ __:_     `. |  ,  `       `    \\
       | ( ,-.`-.    ;'  ;   `       :    ;
       | |  ,   `.      /     ;      :    \\
       ;-'`:::._,`.__),'             :     ;
      / ,  `-   `--                  ;     |
     /  \                   `       ,      |
    (    `     :              :    ,\      |
     \   `.    :     :        :  ,'  \    :
      \    `|-- `     \ ,'    ,-'     :-.-';
      :     |`--.______;     |        :    :
       :    /           |    |         |   \\
       |    ;           ;    ;        /     ;
     _/--' |           :`-- /         \_:_:_|
   ,',','  |           |___ \\
   `^._,--'           / , , .)
                      `-._,-'
                BENEK
''')
    key_pressed()
    print('''Benek: Woof woof! 
Benek: What are you doing here?\n''')
    key_pressed()
    print(f"{player['Name']}: Hi! I'm {player['Name']}, I lost my human. Did you see him?\n")
    key_pressed()
    print("Benek: I don't know. There are lot of humans. How does your looks?\n")
    key_pressed()
    print(f"{player['Name']}: My human... He smell like sausage and taste like ham. Did you see him?\n")
    key_pressed()
    print("Benek: ... Yes, I did. I can show you which way he went. But first, you have to help me.\n")
    key_pressed()
    print(f"{player['Name']}: Can you first show me and then I will help you?\n")
    key_pressed()
    print("Benek: No.\n")
    key_pressed()
    print(f"{player['Name']}: Ok, so... How can I help you?\n")
    key_pressed()
    print('''
          __,-----._                       ,-.
        ,'   ,-.    \`---.          ,-----<._/
       (,.-. o:.`    )),"\\-._    ,'         `.
      ('"-` .\       \`:_ )\  `-;'-._          \\
     ,,-.    \` ;  :  \( `-'     ) -._     :   `:
    (    \ `._\\ ` ;             ;    `    :    )
     \`.  `-.    __   ,         /  \        ;, (
      `.`-.___--'  `-          /    ;     | :   |
        `-' `-.`--._          '           ;     |
              (`--._`.                ;   /\    |
               \     '                \  ,  )   :
               |  `--::----            \'   ;  ;|
               \    .__,-      (        )   :  :|
                \    : `------; \      |    |   ;
                 \   :       / , )     |    |  (
                  \   \      `-^-|     |   / , ,\\
                   )  )          | -^- ;   `-^-^'
                _,' _ ;          |    |
               / , , ,'         /---. :
               `-^-^'          (  :  :,'
                                `-^--'
                    BENEK\n''')
    print("Benek: I saw few mouses over there. They are stealing my food. We need to hunt them. Can you do that?\n")
    key_pressed()
    print(f"{player['Name']}: Of course I can! Show me where are they!\n")
    key_pressed()
    util.clear_screen()

def second_dialogue_with_Benek(player):
    util.clear_screen()
    print('''
         ,--._______,-.
       ,','  ,    .  ,_`-.
      / /  ,' , _` ``. |  )       `-..
     (,';'""`/ '"`-._ ` \/ ______    \\
       : ,o.-`- ,o.  )\` -'      `---.))
       : , d8b ^-.   '|   `.      `    `.
       |/ __:_     `. |  ,  `       `    \\
       | ( ,-.`-.    ;'  ;   `       :    ;
       | |  ,   `.      /     ;      :    \\
       ;-'`:::._,`.__),'             :     ;
      / ,  `-   `--                  ;     |
     /  \                   `       ,      |
    (    `     :              :    ,\      |
     \   `.    :     :        :  ,'  \    :
      \    `|-- `     \ ,'    ,-'     :-.-';
      :     |`--.______;     |        :    :
       :    /           |    |         |   \\
       |    ;           ;    ;        /     ;
     _/--' |           :`-- /         \_:_:_|
   ,',','  |           |___ \\
   `^._,--'           / , , .)
                      `-._,-'
                BENEK
''')
    print("Benek: Thank you my friend! You beat them! Do you want to stay in my hideout?\n")
    key_pressed()
    print(f"{player['Name']}: I don't know. I should probably look for my human now.\n")
    key_pressed()
    print("Benek: You're not going to find anything in the night. You better stay with me and in the morning I can show you which way he went.\n")
    key_pressed()
    print(f"{player['Name']}: Ok then. Let's go.\n")
    key_pressed()
    util.clear_screen()

def third_dialogue_with_Benek(player):
  util.clear_screen()
  print("Benek: Here you go, you probably want to take some food on the road.\n")
  key_pressed()
  print(f"{player['Name']}: Thank you! Do you think I'm gonna find my human?\n")
  key_pressed()
  print("Benek: Of course you are!\n")
  key_pressed()
  print("Benek: It's going to be long journey. Take it.")
  print('''
       .-.               .-.
      (   `-._________.-'   )
       >=     _______     =<
      (   ,-'`       `'-,   )
       `-'               `-'   
''')
  key_pressed
  print("Benek: Take this too.\n")
  print('''
           .--._ 
         \ ).'
          )|/
         ''''_.''''-._
       (        \\
        \        )
        )'-.    (
       /     _.-'\\
      /           )
     ('-._       /
      \        _/      
       '-.__==''  
       ''')
  key_pressed()
  print(f"{player['Name']}: Ewww! What's that? It smells so bad..\n")
  key_pressed()
  print("Benek: I don't know. It works on cats. Meybe you're going to need this.\n")
  key_pressed()
  print(f"{player['Name']}: Thank you. Be well my friend\n!")
  key_pressed()
  util.clear_screen()

def dialogue_with_cat(player):
  util.clear_screen()
  print(f"{player['Name']}: Oh my Dog! You scared me!\n")
  key_pressed()
  print('''

          _..---...,""-._     ,/}/)
       .''        ,      ``..'(/-<
      /   _      {      )         \\
     ;   _ `.     `.   <         a(
   ,'   ( \  )      `.  \ __.._ .: y
  (  <\_-) )'-.____...\  `._   //-'
   `. `-' /-._)))      `-._)))
     `...'         
            STRIPE
''')
  print("Stripe: Is it a collar?\n")
  key_pressed()
  print(f"{player['Name']}: Yes, why?\n")
  key_pressed()
  print("Stripe: Why are you wearing it? Do you have home?\n")
  key_pressed()
  print(f"{player['Name']}: I lost my human. Did you see him?\n")
  key_pressed()
  print("Stripe: So you don't have home... give me that collar you little dog!\n")
  key_pressed()
  print(f"{player['Name']}: I don't want to...\n")
  key_pressed()
  print("Stripe: You will regret it MEOOOOOOW!!!\n")

def second_dialogue_with_cat(player):
  util.clear_screen()
  print('''
         .--._ 
         \ ).'
          )|/
         ''''_.''''-._
       (        \\
        \        )
        )'-.    (
       /     _.-'\\
      /           )
     ('-._       /
      \        _/      
       '-.__==''  

    SACK WITH CATMINT
\n''')
  
  key_pressed()
  print("Stripe: What's that? Smells so goooood...\n")
  print('''
                __..--''``---....___   _..._    __
    /// //_.-'    .-/";  `        ``<._  ``.''_ `. / // /
   ///_.-' _..--.'_    \                    `( ) ) // //
   / (_..-' // (< _     ;_..__               ; `' / ///
    / // // //  `-._,_)' // / ``--...____..-' /// / //

                STRIPE
    ''')
  key_pressed()
  print(f"{player['Name']}: I'm.. gonna... go...\n")
  key_pressed()
  util.clear_screen


def dialogue_with_boar(player):
  print('''
  
              _,-""""-..__
         |`,-'_. `  ` ``  `--'""".
         ;  ,'  | ``  ` `  ` ```  `.
       ,-'   ..-' ` ` `` `  `` `  ` |==.
     ,'    ^    `  `    `` `  ` `.  ;   \\
    `}_,-^-   _ .  ` \ `  ` __ `   ;    #
       `"---"' `-`. ` \---""`.`.  `;
                  \\` ;       ; `. `,
                   ||`;      / / | |
                  //_;`    ,_;' ,_;"
                  
                MR BOAR
''')
  print("Mr Boar: Oink oink!\n")
  key_pressed()
  print(f"{player['Name']}: *sneaking*\n")
  key_pressed()
  print("Mr Boar: YOU! I'M GONNA RAM YOU!!!!!!!\n")
  key_pressed()

def telling_the_story():
  print('\nFrom the beginning...\n\n\n')
  sleep(3)
  print('''
                      _,)
            _..._.-;-'
        .-'     `(
       /      ;   \\
      ;.' ;`  ,;  ;
     .'' ``. (  \ ;
    / f_ _L \ ;  )\\
    \/|` '|\/;; <;/
   ((; \_/  (()       
      \n''')
  print('There was a little dog living with his Owner in small flat.\n')
  sleep(10)
  print('One day the Owner decide to go for a walk to nearest park.\n')
  sleep(10)
  print('When they came there, it turn out that a lot of people came up with the same idea...\n')
  sleep(10)
  print("It wouldn't be any difference, but it was. They were going to find out in few more minutes.\n")
  sleep(10)
  print('''
          _._
        .'--.`.
        |  .' |  
         `--`'
              ''')
  print('Owner started throwing the tennis ball\n')
  sleep(10)
  print('Dog ran for the ball... and got lost\n')
  sleep(10)
  print('Owner was trying to find little dog, but it disappered...')
  sleep(10)