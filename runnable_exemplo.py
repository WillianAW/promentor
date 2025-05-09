from langchain_core.runnables import RunnableLambda

def add_one(x: int) -> int:
    return x + 1 

def mul_two(x: int) -> int: 
    return x + 2 

def mul_three(x: int) -> int: 
    return x + 3 

runnable_1 = RunnableLambda(add_one)
runnable_2 = RunnableLambda(mul_two)
runnable_3 = RunnableLambda(mul_three)

sequence = runnable_1 | {
    "mul_two": runnable_2,
    "mul_three": runnable_3,
}




resposta = sequence.invoke(1)

print(runnable_1.invoke(1))
print(runnable_2.invoke(2))
print(resposta)