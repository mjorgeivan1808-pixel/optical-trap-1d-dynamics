# optical-trap-1d-dynamics
Animación interactiva de una partícula atrapada ópticamente en 1D con fuerza gradiente, fuerza de radiación en la zona central y amortiguamiento viscoso. Muestra la evolución temporal hacia el equilibrio.
# Dinámica 1D de una trampa óptica – Animación interactiva

Simulación y visualización animada del movimiento de una partícula en una trampa óptica unidimensional. La partícula está sometida a una fuerza de gradiente (restauradora), una fuerza de radiación constante dentro de una región central, y una fuerza de arrastre viscoso. El sistema se resuelve numéricamente mediante el método de Euler y se representa cuadro a cuadro con `matplotlib.animation`.

---

## 🧠 Modelo físico

En la aproximación unidimensional, una partícula de masa \(m=1\) se mueve bajo las siguientes fuerzas:

- **Fuerza de gradiente** \(F_{\text{grad}} = -k x\), que atrae la partícula hacia el centro \(x=0\) (potencial armónico).
- **Fuerza de radiación** \(F_{\text{rad}}\): actúa solo cuando la partícula se encuentra en la región central \(|x| \le x_{\text{umbral}}\), empujándola en la dirección positiva del eje \(x\). Representa, por ejemplo, la presión de radiación debida a un segundo haz o a un desbalance en el enfoque.
- **Fuerza de arrastre** \(F_{\text{drag}} = -\gamma v\), proporcional a la velocidad (amortiguamiento viscoso).

La ecuación de movimiento (sin ruido térmico) es:

\[
\frac{d^2 x}{dt^2} = -k x + F_{\text{rad}}(x) - \gamma \frac{dx}{dt}
\]

donde \(F_{\text{rad}}(x) = F_{\text{rad\_value}}\) si \(|x| \le x_{\text{umbral}}\) y 0 en caso contrario.

La integración se realiza con el método de Euler simple:

\[
\begin{aligned}
v_{t+dt} &= v_t + (F_{\text{grad}} + F_{\text{rad}} + F_{\text{drag}}) \, dt \\
x_{t+dt} &= x_t + v_{t+dt} \, dt
\end{aligned}
\]

La animación muestra cómo la partícula, inicialmente alejada del centro, oscila y eventualmente se estabiliza debido al amortiguamiento, pudiendo quedar atrapada en una posición de equilibrio donde las fuerzas se cancelan.

---

## 🚀 Uso

1. Asegúrate de tener instaladas las dependencias:
   ```bash
   pip install numpy matplotlib
