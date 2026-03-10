%{
#include <stdio.h>
#include <math.h>

int yylex();
void yyerror(char *s);

double raiz(double n){
    double x = n;
    double error = 0.00001;

    while(fabs(x - n/x) > error){
        x = 0.5 * (x + n/x);
    }

    return x;
}
%}

%union {
    double num;
}

%token <num> NUM
%token EOL

%%

input:
      NUM EOL { printf("Raiz cuadrada = %lf\n", raiz($1)); }
      ;

%%

void yyerror(char *s){
    printf("Error: %s\n", s);
}

int main(){
    printf("Ingrese un numero:\n");
    yyparse();
    return 0;
}
