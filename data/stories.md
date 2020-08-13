## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy
  - utter_can_i_help

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_can_i_help

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_can_i_help

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
 
 ## nada
 * nada
   - action_listen

 
 ## gracias
 * gracias
   - utter_gracias
   - utter_can_i_help_more
 * affirm
    - utter_can_i_help

  ## gracias no
  * gracias
    - utter_gracias
    - utter_can_i_help_more
  * deny
    - utter_goodbye
    
 ## que_podes_hacer
 * que_podes_hacer
   - utter_que_podes_hacer

## interactive_story_3
* greet
    - utter_greet
* mood_great
    - utter_happy
* ask_time
    - action_respond_time

## ask for time
* ask_time
    - action_respond_time

## ask for address
* ask_address
    - action_respond_address

## ask for date
* ask_date
    - action_respond_date

## interactive_story_1
* handle_insult
    - utter_handle_insult

## interactive_story_1
* human_handoff
    - utter_human_handoff

## interactive_story_1
* ask_address{"dependencia": "gestion humana"}
    - action_respond_address

## interactive_story_1
* ask_address{"dependencia": "direccion de gestion humana"}
    - action_respond_address
    
## interactive_story_1
* ask_address{"dependencia": "direccion de informatica"}
    - action_respond_address

## interactive_story_1
* ask_address{"dependencia": "direccion de informatica"}
    - action_respond_address
    
## interactive_story_1
* ask_address{"dependencia": "tribunal superior de justicia"}
    - action_respond_address
    
## interactive_story_1
* ask_address{"dependencia": "oficina de familia"}
    - action_respond_address
    
## interactive_story_1
* ask_address{"dependencia": "direccion de informatica"}
    - action_respond_address
 
## interactive_story_1
* ask_address{"dependencia": "kiosco"}
    - action_respond_address
    
## interactive_story_1
* ask_address{"dependencia": "tribunal superior"}
    - action_respond_address

## interactive_story_1
* ask_address{"dependencia": "direccion general de informatica"}
    - action_respond_address

## interactive_story_1
* ask_address{"dependencia": "juzgado"}
    - action_respond_address
    
## interactive_story_1
* ask_address{"dependencia": "juzgado"}
    - action_respond_address

## interactive_story_1
* ask_address{"dependencia": "rpc"}
    - action_respond_address

## interactive_story_1
* ask_address{"dependencia": "oficina"}
    - action_respond_address

## interactive_story_1
* ask_address{"dependencia": "juzgado de paz"}
    - action_respond_address
    
## interactive_story_1
* ask_address{"dependencia": "direccion general de informatica"}
    - action_respond_address
    
## interactive_story_1
* ask_address{"dependencia": "juzgado de paz"}
    - action_respond_address
    
## interactive_story_1
* ask_address{"dependencia": "juzgado de paz"}
    - action_respond_address
    
## interactive_story_1
* ask_address{"dependencia": "mesa de entrada"}
    - action_respond_address
