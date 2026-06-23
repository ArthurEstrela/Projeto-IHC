# Projeto Final de IHC — Avaliação da Usabilidade do Stylo

Dupla: **Arthur Faria Estrela e Sávio Issa de Sousa** · IF Goiano – Campus Urutaí · 7º Período · Disciplina: IHC.

## O que entregar / abrir

| Arquivo | O que é |
|---|---|
| **`Projeto_Final_IHC.docx`** | Documento final editável (Word), seções 1 a 9 do modelo, com tabelas e gráficos. **É o arquivo principal de entrega.** |
| **`Projeto_Final_IHC.html`** | Mesma versão formatada para leitura/impressão. Abra no navegador e use **Imprimir → Salvar como PDF** (A4). |
| **`prototipo/index.html`** | **Protótipo navegável** (Seção 7). Abra no navegador e clique para navegar. O botão *"Mostrar melhorias"* destaca cada correção. |

## Estrutura do documento (conforme o modelo)
1. Produto a ser avaliado · 2. Framework DECIDE · 3. Avaliação heurística · 4. Experimento (planejado + piloto + realizado) · 5. Resultados (tabelas e gráficos) · 6. Discussão · 7. Proposta de melhorias + protótipo · 8. Conclusão · 9. Referências.

## Como navegar no protótipo
- **Login** → link "Esqueci minha senha" (melhoria da heurística 3).
- **Painel · Equipe** → "Equipe" agora é item de primeiro nível + botão "+ Adicionar profissional".
- **Painel · Financeiro** → filtros de período maiores.
- **Agendamento (cliente)** → serviços com preço de alto contraste → profissional → calendário com indicadores de vaga e "Próximo horário livre" → modal de aviso antes do login → confirmação.

## Regenerar (opcional)
Requer Python com `python-docx` e `matplotlib`:
```bash
python gen_charts.py   # gera os gráficos em assets/
python build_doc.py    # gera o .docx e o .html
```

> Observação: as figuras 5–8 do documento são capturas reais do protótipo. Os dados de teste (matriz de tarefas, SUS 78,3, incidentes do Think-Aloud) vieram dos relatórios já produzidos pela dupla; o teste do protótipo (Fig. 9) é uma validação rápida com 3 usuários.
