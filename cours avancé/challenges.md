## Utiliser [GPT Crawler](https://github.com/BuilderIO/gpt-crawler) pour: 
-  Faire une application qui traduit texte et voix pour produire une application du type [Livre audio](https://learnpythonfast.up.railway.app/) à partir d'une structure arborescente de type markdown( comme formationIA2.0)
-  Faire un chatbot qui peut répondre à toutes les questions liées à une structure arborescente en markdown/ 

## ChatGPT local
-  Faire un équivalent d'un GPTs d'OpenAI en local open source (avec scraping des GPTs d'openAI)
  
## Emulateur de microcontrôleur
- Faire un Chatbot qui écrit du code pour un microcontrôleur et qui le valide sur un [émulateur](https://github.com/lrusso/ArduinoSimulator)
## Rendre un LLM local open source plus performant que GPT4 turbo:
- En l'alimentant avec les bases de données pertinentes
- Avec [Pinecone](https://www.pinecone.io/blog/rag-study/)

- ![Capture d'écran 2024-01-17 090906](https://github.com/jpbrasile/formationIA2.0/assets/8331027/9f15f1a5-69e0-4b0a-9db5-1cfa67aea343)

## Concevoir un LLM efficace pour coder
[AlphaCodium](https://github.com/Codium-ai/AlphaCodium/tree/main) :[Premières discussions avec ChatGPT](https://chat.openai.com/share/d71b9fb2-2e41-4ec6-8219-6ecf2b8842e0)
### LLLM open source fait mieux que ChatGPT4 
![Capture d'écran 2024-01-19 105926](https://github.com/jpbrasile/formationIA2.0/assets/8331027/3d135c46-d7b2-413b-a388-2624c8f080ef) 
[référence](https://www.codium.ai/blog/alphacodium-state-of-the-art-code-generation-for-code-contests/)
### [Base du prompt](https://github.com/Codium-ai/AlphaCodium?tab=readme-ov-file) 
First and foremost, we feel that the proposed AlphaCodium flow, with reasonable adjustments, can be used as a more general framework for other code generation tasks.

Secondly, many of the design concepts, principles, and tricks we acquired in this work are broadly applicable as-is to any general code generation tasks. For example:

YAML Structured output: asking the model to generate an output in YAML format, equivalent to a given Pydantic class
Semantic reasoning via bullet points analysis: bullet points analysis encourage an in-depth understanding of the problem, and force the model to divide the output into logical semantic sections, leading to improved results
LLMs do better when generating a modular code: when clearly asking the model to: divide the generated code into small sub-functions, with meaningful names and functionality, we observe a better-produced code, with fewer bugs, and higher success rates for the iterative fixing stages.
Soft decisions with double validation: with a double validation process, we add an extra step where, given the generated output, the model is asked to re-generate the same output, but correct it if needed
Leave room for exploration: since the model can be wrong, it’s better to avoid irreversible decisions, and leave room for exploration and code iterations with different possible solutions
### [Prompt généré par Grimoire](https://chat.openai.com/share/b20dde21-744a-4e48-b854-c422a38762ce) qui suit ce type de template:
1. Problem Reflection
Task: Describe the problem for {specific problem to code}.
Output: Bullet points detailing the problem goal, inputs, outputs, rules, constraints, and other relevant details.
2. Public Tests Reasoning
Task: Explain why each public test input leads to its respective output for {specific problem to code}.
Output: Bullet points or paragraphs explaining the reasoning behind each test case.
3. Generate Possible Solutions
Task: Create 2-3 possible solutions in natural language for {specific problem to code}.
Output: YAML object equivalent to type $PossibleSolutions, detailing each solution's name, content, rationale, and complexity.
4. Rank Solutions
Task: Rank the generated solutions for {specific problem to code}.
Criteria: Correctness, simplicity, robustness (not necessarily efficiency).
Output: The best solution is chosen based on the criteria.
5. Generate Additional AI Tests
Task: Develop 6-8 diverse input-output tests for {specific problem to code}.
Output: Tests covering cases not addressed by public tests, such as large inputs and edge cases.
6. Initial Code Solution
Task: Generate an initial code solution for {specific problem to code}.
Process:
Choose a potential solution.
Generate corresponding code.
Run on selected public and AI tests.
Repeat until tests pass or a try-limit is reached.
Use the first passing or closest output code as the base.
7. Iterate on Public Tests
Task: Iteratively run and fix the base code on public tests for {specific problem to code}.
Output: Improved code that passes all public tests.
8. Iterate on AI-generated Tests
Task: Continue iterations on AI-generated tests for {specific problem to code}.
Output: Final code that passes both public and AI-generated tests.
Additional Notes:
Knowledge Accumulation: Progress from easy to difficult stages, using insights from earlier stages to aid in more challenging ones.
Modular Code Generation: Divide generated code into small, well-named sub-functions.
Soft Decisions with Double Validation: Re-validate generated outputs, correcting errors if needed.
Gradual Data Accumulation: Start with easier tasks, moving to harder ones only after gaining sufficient insights.
Test Anchors: Use passed tests as anchors to validate the correctness of code against AI-generated tests.
