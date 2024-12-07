from langchain_openai import ChatOpenAI
from state import SupportState
from templates import greeting_template,issue_analysis_template,satisfaction_template,issue_acknowledgement,inspection_template,decorator_template
from langgraph.graph import END,START,StateGraph
import os 
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.9, api_key=os.getenv('OPENAI_API_KEY'))

def greet_the_user(state : SupportState):
    prompt = greeting_template.format(name=state['name'])
    response = llm.predict(prompt)
    print(response)
    print('\n'*7)
    return state

def identify_issue(state : SupportState):
    prompt = issue_acknowledgement.format(name =state['name'])
    response = llm.predict(prompt)
    print(response)
    print('\n'*7)

    return state

def provide_solution(state : SupportState):
    prompt = issue_analysis_template.format(issue=state['issue'])
    response = llm.predict(prompt)
    state['solution'] = response
    print(response)
    return state

def __inspector__(state : SupportState):
    
    inspection_count = state.get("inspection_count", 0)

    solution  = state.get("solution","No solution was found")
    
    prompt = inspection_template.format(solution=solution)
    llm_feedback = llm.predict(prompt)
    
    print('\n'*2)
    print(f"LLM Feedback : {llm_feedback}")
    
    if 'yes' in llm_feedback.lower():
        state['solution_approved'] = True
        print('Solution is approved by - Dev')
    else:
        state['solution_approved'] = False
        print('Dev has ordered another Solution')
        inspection_count += 1
        state['inspection_count'] = inspection_count
        
        if inspection_count >= 3:  
            state['solution_approved'] = True  
            print('Solution is automatically approved after attempts.')
    return state

def should_condition_after_inspection(state : SupportState): #Always return Nodes in should condition
    if state.get('solution_approved',False):
        return 'end_state'
    
    return 'provide_solution'   

def end_function(state : SupportState):
    return state

































































# def output_decorator(state: SupportState):
#     #   prompt = decorator_template.format(solution=state['solution'])
    
#     #   generated_solution = llm.predict(prompt)
#     #   state['final_solution'] = generated_solution
#     #   print(f"Final Generated Solution: {generated_solution}")
#     #   return state
#     final_solution  = state.get("solution","No solution was found")
    
#     prompt = decorator_template.format(solution=final_solution)
#     llm_feedback = llm.predict(prompt)
#     print(llm_feedback)
#     return state



        