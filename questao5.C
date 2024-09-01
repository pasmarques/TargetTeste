#include <stdio.h>
#include <string.h>

// Já tinha feito uma questão dessa na faculdade, então por isso escolhi C

void inverterString(char *str) {
    int esquerda = 0; // Primeiro Caractere válido
    int direita = strlen(str) - 1; // Último caractere válido
    char temp; // Variável auxiliar para a troca

    // Troca os caracteres da esquerda e direita até o meio da string
    while (esquerda < direita) {
        temp = str[esquerda];
        str[esquerda] = str[direita];
        str[direita] = temp;
        esquerda++;
        direita--;
    }
}

int main() {
    char str[100];

    printf("Digite uma string: ");
    fgets(str, sizeof(str), stdin);
    
    // Remover o caractere de nova linha, se presente
    str[strcspn(str, "\n")] = '\0';

    inverterString(str); // Chama a função criada para reverter string

    printf("String invertida: %s\n", str);

    return 0;
}