For some reason I thought that it'll be cool to have a neural network that can be used to calculate the mean of a stream of data, updating the mean after each data point. I thought I could feed the mean back into the network as an input, along with a data point. However, it is stupid to use a network for such a trivial task -
$$
    \bar{x}_i = \frac{(i-1)\times \bar{x}_{i-1} + x_i}{i}
$$

So, I decided to implement a simple algorithm which maintains two weights: one weight, $m$, for the current mean, and one weight, $n$, for the new data point. 
$$
    \bar{x}_n = m\times\bar{x}_{i-1} + n\times x_i
$$
In each iteration, these weights are updated as
$$\begin{align*}
    m &= \frac{1}{2-m} \\
    n &= \frac{n}{n+1}
\end{align*}$$