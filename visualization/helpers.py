import matplotlib.pyplot as plt
import pandas as pd

from qr.ml.evaluation.plot import colors
import numpy as np
import seaborn as sns


def numerical_dist_plot_target(df, numerical_feats, target, theme='blues', save_plot=True, path=None):
    fig = plt.figure(figsize=(12, 12), dpi=150, facecolor=colors.PLAIN_BACKGROUND)
    gs = fig.add_gridspec(4, 3)
    gs.update(wspace=0.1, hspace=0.4)


    plot = 0
    for row in range(0, 1):
        for col in range(0, 3):
            locals()["ax" + str(plot)] = fig.add_subplot(gs[row, col])
            locals()["ax" + str(plot)].set_facecolor(colors.PLAIN_BACKGROUND)
            locals()["ax" + str(plot)].tick_params(axis='y', left=False)
            locals()["ax" + str(plot)].get_yaxis().set_visible(False)
            for s in ["top", "right", "left"]:
                locals()["ax" + str(plot)].spines[s].set_visible(False)
            plot += 1

    plot = 0
    s = df[df[target] == 1]
    ns = df[df[target] == 0]
    for feature in numerical_feats[1:]:
        sns.kdeplot(s[feature], ax=locals()["ax" + str(plot)], color=colors[0], shade=True, linewidth=1.5, ec='black',
                    alpha=0.9, zorder=3, legend=False)
        sns.kdeplot(ns[feature], ax=locals()["ax" + str(plot)], color=colors[2], shade=True, linewidth=1.5, ec='black',
                    alpha=0.9, zorder=3, legend=False)
        locals()["ax" + str(plot)].grid(which='major', axis='x', zorder=0, color='gray', linestyle=':', dashes=(1, 5))

        plot += 1

    ax0.set_xlabel('Age')
    ax1.set_xlabel('Avg. Glucose Levels')
    ax2.set_xlabel('BMI')
    ax0.text(-20, 0.056, 'Numeric Variables by Stroke & No Stroke', fontsize=20, fontweight='bold', fontfamily='serif')
    if save_plot:
        save_path = '' + path + '/' if path is not None else ''
        plt.savefig(save_path + 'Numerical_Distribution.pdf')

    plt.show()

    return


def numerical_dist_plot(df, numerical_feats, target, theme='blues', save_plot=True, path=None):
    ...





