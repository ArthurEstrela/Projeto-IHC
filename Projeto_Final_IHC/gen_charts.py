# -*- coding: utf-8 -*-
"""Gera os gráficos do Projeto Final de IHC (avaliação de usabilidade do Stylo)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np
import os

OUT = os.path.join(os.path.dirname(__file__), "assets")
os.makedirs(OUT, exist_ok=True)

# Paleta coesa (tinta / creme / clay / sálvia)
INK     = "#1A1714"
CREAM   = "#F6F1E9"
PAPER   = "#FBF8F2"
CLAY    = "#C2603F"
CLAY_L  = "#E0A487"
SAGE    = "#7C8A6B"
SAND    = "#D9C7A8"
GREY    = "#9B9085"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "text.color": INK,
    "axes.edgecolor": "#D8CBB7",
    "axes.labelcolor": INK,
    "xtick.color": INK,
    "ytick.color": INK,
    "axes.linewidth": 1.0,
    "figure.dpi": 130,
})

tasks = ["T1\nCadastrar\ncliente", "T2\nAdd\nprofissional", "T3\nDefinir\nserviço",
         "T4\nDefinir\ndisponib.", "T5\nAgend.\ninteligente", "T6\nAceitar\nagend.",
         "T7\nConcluir\nserviço", "T8\nInterpretar\nmétricas"]
sem_ajuda = [6, 4, 5, 4, 6, 6, 6, 5]
com_ajuda = [0, 2, 1, 2, 0, 0, 0, 1]
tempos    = [45, 110, 55, 130, 30, 15, 20, 65]  # segundos

# ---------------------------------------------------------------- GRÁFICO 1
# Taxa de conclusão por tarefa (barras empilhadas)
def grafico_conclusao():
    fig, ax = plt.subplots(figsize=(9.2, 4.6))
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)
    x = np.arange(len(tasks))
    b1 = ax.bar(x, sem_ajuda, width=0.62, color=SAGE, label="Concluída sem ajuda", zorder=3)
    b2 = ax.bar(x, com_ajuda, width=0.62, bottom=sem_ajuda, color=CLAY, label="Concluída com ajuda", zorder=3)
    for i in range(len(tasks)):
        if sem_ajuda[i]:
            ax.text(i, sem_ajuda[i]/2, str(sem_ajuda[i]), ha="center", va="center",
                    color="white", fontweight="bold", fontsize=11)
        if com_ajuda[i]:
            ax.text(i, sem_ajuda[i]+com_ajuda[i]/2, str(com_ajuda[i]), ha="center", va="center",
                    color="white", fontweight="bold", fontsize=10)
    ax.set_ylim(0, 7)
    ax.set_yticks(range(0, 7))
    ax.set_xticks(x)
    ax.set_xticklabels(tasks, fontsize=8.5)
    ax.set_ylabel("Nº de participantes (de 6)")
    ax.set_title("Taxa de conclusão das tarefas — 6 participantes",
                 fontsize=13, fontweight="bold", pad=14, loc="left")
    ax.grid(axis="y", color="#E6DCC9", zorder=0)
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    ax.legend(frameon=False, loc="lower right", fontsize=9.5, ncol=2)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "grafico_conclusao.png"), facecolor=PAPER, bbox_inches="tight")
    plt.close(fig)

# ---------------------------------------------------------------- GRÁFICO 2
# Tempo médio por tarefa (barras horizontais)
def grafico_tempo():
    fig, ax = plt.subplots(figsize=(9.2, 4.6))
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)
    labels = [t.replace("\n", " ") for t in tasks]
    y = np.arange(len(labels))[::-1]
    cores = [CLAY if v >= 90 else SAGE for v in tempos]
    ax.barh(y, tempos, color=cores, height=0.62, zorder=3)
    for i, v in enumerate(tempos):
        m, s = divmod(v, 60)
        txt = f"{m}m{s:02d}s" if m else f"{s}s"
        ax.text(v + 2, y[i], txt, va="center", ha="left", fontsize=9.5, color=INK)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=9)
    ax.set_xlim(0, 150)
    ax.set_xlabel("Tempo médio (segundos)")
    ax.set_title("Tempo médio de execução por tarefa",
                 fontsize=13, fontweight="bold", pad=14, loc="left")
    ax.grid(axis="x", color="#E6DCC9", zorder=0)
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    # legenda manual
    from matplotlib.patches import Patch
    leg = [Patch(facecolor=SAGE, label="Fluxo fluido (< 90s)"),
           Patch(facecolor=CLAY, label="Ponto de atrito (≥ 90s)")]
    ax.legend(handles=leg, frameon=False, loc="lower right", fontsize=9.5)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "grafico_tempo.png"), facecolor=PAPER, bbox_inches="tight")
    plt.close(fig)

# ---------------------------------------------------------------- GRÁFICO 3
# Medidor SUS (gauge semicircular)
def grafico_sus():
    score = 78.3
    fig, ax = plt.subplots(figsize=(7.6, 4.4), subplot_kw={"aspect": "equal"})
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)
    # faixas de referência do SUS
    faixas = [(0, 51, "#C0392B", "Ruim"),
              (51, 68, "#E0A487", "OK"),
              (68, 80.3, "#C2603F", "Bom"),
              (80.3, 100, "#7C8A6B", "Excelente")]
    import matplotlib.patches as mpatches
    R, r = 1.0, 0.62
    for a0, a1, col, _ in faixas:
        t0 = 180 - (a0 / 100 * 180)
        t1 = 180 - (a1 / 100 * 180)
        ax.add_patch(mpatches.Wedge((0, 0), R, t1, t0, width=R - r, facecolor=col, edgecolor=PAPER, lw=2))
    # ponteiro
    ang = np.radians(180 - score / 100 * 180)
    ax.plot([0, 0.80 * np.cos(ang)], [0, 0.80 * np.sin(ang)], color=INK, lw=3.2, zorder=5)
    ax.add_patch(mpatches.Circle((0, 0), 0.045, color=INK, zorder=6))
    ax.text(0, -0.22, f"{score:.1f}", ha="center", va="center", fontsize=34, fontweight="bold", color=INK)
    ax.text(0, -0.42, "SUS Score — média de 6 participantes", ha="center", va="center", fontsize=10.5, color=GREY)
    ax.text(0, -0.56, "Classificação: BOM / quase Excelente   ·   percentil ~80   ·   nota B+", ha="center", va="center", fontsize=9, color=CLAY)
    # marcações
    for val in [0, 25, 50, 68, 75, 100]:
        a = np.radians(180 - val / 100 * 180)
        ax.text(1.12 * np.cos(a), 1.12 * np.sin(a), str(val), ha="center", va="center", fontsize=8.5, color=GREY)
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-0.7, 1.3)
    ax.axis("off")
    ax.set_title("Pontuação SUS (System Usability Scale)", fontsize=13, fontweight="bold", pad=2, loc="center")
    fig.savefig(os.path.join(OUT, "grafico_sus.png"), facecolor=PAPER, bbox_inches="tight")
    plt.close(fig)

# ---------------------------------------------------------------- GRÁFICO 4
# Problemas de usabilidade por severidade / origem (donut)
def grafico_problemas():
    # Consolidado da avaliação heurística + think-aloud
    cat = ["Crítico", "Sério", "Moderado", "Cosmético"]
    val = [2, 4, 5, 3]
    cores = ["#C0392B", CLAY, CLAY_L, SAND]
    fig, ax = plt.subplots(figsize=(6.6, 4.4))
    fig.patch.set_facecolor(PAPER)
    wedges, _ = ax.pie(val, colors=cores, startangle=90, counterclock=False,
                       wedgeprops=dict(width=0.42, edgecolor=PAPER, linewidth=2))
    ax.text(0, 0.12, str(sum(val)), ha="center", va="center", fontsize=30, fontweight="bold", color=INK)
    ax.text(0, -0.16, "problemas\nidentificados", ha="center", va="center", fontsize=9.5, color=GREY)
    leg = [f"{c} — {v}" for c, v in zip(cat, val)]
    ax.legend(wedges, leg, frameon=False, loc="center left", bbox_to_anchor=(1.0, 0.5), fontsize=10.5)
    ax.set_title("Problemas de usabilidade por severidade",
                 fontsize=13, fontweight="bold", pad=10, loc="left")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "grafico_problemas.png"), facecolor=PAPER, bbox_inches="tight")
    plt.close(fig)

# ---------------------------------------------------------------- GRÁFICO 5
# Teste do protótipo: antes x depois (tempo / sucesso nas tarefas críticas)
def grafico_prototipo():
    fig, ax = plt.subplots(figsize=(9.2, 4.4))
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)
    labels = ["T2 — Localizar\n'Equipe'", "Ver preço\ndo serviço", "Achar dia\ncom vaga", "Redirec.\np/ login"]
    antes = [110, 18, 40, 0]   # segundos (ou indicador)
    depois = [22, 5, 8, 0]
    x = np.arange(len(labels))
    w = 0.36
    ax.bar(x - w/2, antes, w, label="Versão atual", color=SAND, zorder=3)
    ax.bar(x + w/2, depois, w, label="Protótipo redesenhado", color=CLAY, zorder=3)
    for i in range(len(labels)):
        ax.text(x[i]-w/2, antes[i]+2, f"{antes[i]}s", ha="center", fontsize=8.5, color=GREY)
        ax.text(x[i]+w/2, depois[i]+2, f"{depois[i]}s", ha="center", fontsize=8.5, color=CLAY)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel("Tempo até a ação (segundos)")
    ax.set_title("Teste do protótipo — tempo para concluir ações críticas (3 usuários)",
                 fontsize=12.5, fontweight="bold", pad=14, loc="left")
    ax.grid(axis="y", color="#E6DCC9", zorder=0)
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    ax.legend(frameon=False, loc="upper right", fontsize=9.5)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "grafico_prototipo.png"), facecolor=PAPER, bbox_inches="tight")
    plt.close(fig)

for f in (grafico_conclusao, grafico_tempo, grafico_sus, grafico_problemas, grafico_prototipo):
    f()
    print("ok:", f.__name__)
print("Gráficos gerados em", OUT)
