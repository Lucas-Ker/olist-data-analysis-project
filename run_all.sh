#!/bin/bash

# Define a cor verde para as mensagens de sucesso
GREEN='\033[0;32m'
NC='\033[0m' # Sem cor

echo "Iniciando a geração do relatório final..."

# Converte o notebook final para HTML, colocando-o na pasta de outputs
jupyter nbconvert --to html --execute notebooks/05_final_report_for_recruiter.ipynb --output-dir=outputs/

echo -e "${GREEN}Relatório '05_final_report_for_recruiter.html' gerado com sucesso na pasta /outputs!${NC}"