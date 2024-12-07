
from langchain_core.prompts import PromptTemplate


greeting_template = PromptTemplate(
    input_variables=["name"],
    template="Greet the user named {name}."
)

issue_acknowledgement = PromptTemplate(
    input_variables=["name"],
    template="Say that you are there to help the user named {name}. Ask them if they are facing any issues."
)

issue_analysis_template = PromptTemplate(
    input_variables=["issue"],
    template="Analyze the following issue: {issue}.Keep Answer in concise bullet points."
)

inspection_template = PromptTemplate(
    input_variables=["solution"],
    template="Inspect the following solution: {solution}. Provide Feedback so that solution is accurate and concise."
)

satisfaction_template = PromptTemplate(
    input_variables=["solution"],
    template="The user was given the following solution: {solution}. Are they satisfied with it?"
)

decorator_template = PromptTemplate(input_variables=["solution"],template = "Decorate this content into points :{solution}, Make it easy to read.")




























































# from langchain.prompts import PromptTemplate


# greeting_template  = PromptTemplate.from_template("Greet the user named {name} and ask how are they doing today.")

# issue_acknowledgement  = PromptTemplate.from_template("Acknowledge the issue of user named {name} , tell them that you are there to help them and working on providing a solution to their problem")

# issue_analysis_template = PromptTemplate.from_template("The user has reported the following issue : {issue}. Provide a detailed step wise solution to the problem")

# inspection_template = PromptTemplate.from_template("You have generated the following solution: {solution}. Is this solution good enough? Reply with 'yes' if the solution is acceptable or 'no' if it needs improvement.")

# satisfaction_template = PromptTemplate("The user was given the following solution {solution}.Ask whether they are satisfied with the given solution or not ")