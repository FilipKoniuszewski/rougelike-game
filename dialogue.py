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

frames = [frame_1, frame_2, frame_3]

frames_2 = [element_1, element_2, element_3]

def waiting_screen(frames):
  range = 0
  while range <10:
    for frame in frames:
      print(frame)
      sleep(0.5)
      util.clear_screen()
      range += 1

def second_waiting_screen(frames_2):
  range = 0
  while range <10:
    for frame in frames_2:
      print(frame)
      sleep(0.5)
      util.clear_screen()
      range += 1

def dialogue_with_Benek():
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
    print("You: Hi! I'm Dogge, I lost my human. Did you see him?\n")
    key_pressed()
    print("Benek: I don't know. There are lot of humans. How does your looks?\n")
    key_pressed()
    print('You: My human... He smell like sausage and taste like ham. Did you see him?\n')
    key_pressed()
    print("Benek: ... Yes, I did. I can show you which way he went. But first, you have to help me.\n")
    key_pressed()
    print("You: Can you first show me and then I will help you?\n")
    key_pressed()
    print("Benek: No.\n")
    key_pressed()
    print("You: Ok, so... How can I help you?\n")
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
    print("You: Of course I can! Show me where are they!\n")
    key_pressed()
    util.clear_screen()

def second_dialogue_with_Benek():
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
    print("You: I don't know. I should probably look for my human now.\n")
    key_pressed()
    print("Benek: You're not going to find anything in the night. You better stay with me and in the morning I can show you which way he went.\n")
    key_pressed()
    print("You: Ok then. Let's go.\n")
    key_pressed()
    util.clear_screen()
    waiting_screen(frames)

def third_dialogue_with_Benek():
  util.clear_screen()
  print("Benek: Here you go, you probably want to take some food on the road\n")
  key_pressed()
  print("You: Thank you! Do you think I'm gonna find my human?\n")
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
  key_pressed()
  util.clear_screen()
  second_waiting_screen(frames_2)

def dialogue_with_cats():
  pass











def dialogue_with_boar():
  pass





if __name__ == "__main__": 
  #dialogue_with_Benek()
  #key_pressed()
  #second_dialogue_with_Benek()
  third_dialogue_with_Benek()