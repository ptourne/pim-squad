$$
S = (s_{1},s_{2},\dots ,s_{n})
$$

$s_{i}$: Energía restante para $i$ días consecutivos de entrenamiento.

$$
E=(e_{1},e_{2},\dots ,e_{n})
$$

$e_{i}$: Cantidad de esfuerzo del entrenamiento $i$.

$g(i,j)$ Ganancia obtenida del $i$-ésimo entrenamiento dado que estamos en el $j$ día de entrenamiento consecutivo.

$$
g(i,j)=\min{(e_{i},s_{j})}
$$

$$
\forall j\leq i,\  g_{par}(i,j)=\begin{cases}
0 & i=0 \\
g(i,j) & i=1 \\
g(i,j)+g_{max}(i-2) & i>1 \land j=1 \\
g(i,j)+g_{par}(i-1,j-1) & i>1 \land j>1
\end{cases}
$$

$$
g_{max}(i)=\max{\left\{ g_{par}(i,j) \right\}_{j\leq i}}
$$
