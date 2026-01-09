## ⚠️ Aviso Importante

Este repositório foi desenvolvido **exclusivamente para fins de estudo, aprendizado e prática** em bioinformática e ciência de dados. Os métodos, análises e resultados apresentados **não devem ser utilizados para aplicações clínicas, diagnósticas ou decisões médicas**.

O projeto tem caráter **exploratório e educacional**, servindo como base para experimentação com técnicas de aprendizado de máquina aplicadas a sequências biológicas. As interpretações biológicas não substituem análises filogenéticas formais ou validações experimentais.

Utilize este material como referência acadêmica e para fins de aprendizado.

# Alinhamento Global de Sequências Biológicas

Este projeto realiza o **alinhamento global de duas sequências biológicas** no formato FASTA utilizando a biblioteca **Biopython**.  
O alinhamento é feito com o algoritmo de **pairwise alignment**, amplamente utilizado em análises de similaridade entre sequências de DNA, RNA ou proteínas.

---

## 🧬 Objetivo

Comparar duas sequências biológicas e identificar:
- O melhor alinhamento global possível
- A pontuação (score) de cada alinhamento
- A correspondência entre as sequências (query e target)

Os resultados são exportados em **formato TXT** e **CSV** para posterior análise.

---

## 📂 Estrutura do Projeto

```text
.
├── 01.fasta              # Primeira sequência biológica
├── 02.fasta              # Segunda sequência biológica
├── alinhamento.txt       # Resultado do alinhamento em texto
├── alinhamento.csv       # Resultado estruturado em CSV
└── alinhamento.py        # Script principal
