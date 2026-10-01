int evalRPN(char** tokens, int tokensSize) {
    int stack[tokensSize]; 
    int top = -1; 
    int a, b, result; 

    for (int i = 0; i < tokensSize; i++) {
        if (isdigit(tokens[i][0]) || (tokens[i][0] == '-' && isdigit(tokens[i][1]))) {
            stack[++top] = atoi(tokens[i]);
        } else {
            b = stack[top--]; 
            a = stack[top--]; 

            switch (tokens[i][0]) {
                case '+': 
                    result = a + b; 
                    break; 
                case '-': 
                    result = a - b; 
                    break; 
                case '*': 
                    result = a * b; 
                    break; 
                case '/':
                    result = a / b;
                    break; 
            } 
            stack[++top] = result; 
        } 
    } 

    return stack[top]; 
}