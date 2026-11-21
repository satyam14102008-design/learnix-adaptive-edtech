# Learnix AI — Learner Model & Spaced Repetition Algorithms

Learnix AI uses continuous, explainable, and deterministic mathematical modeling rather than arbitrary random increments. The model tracks individual competency, confidence levels, reasoning depth, and forgetting risks for every concept in the syllabus.

---

## 1. Dynamic Mastery Score Update Algorithm

Every student maintains a concept mastery score $M \in [0, 100]$ and confidence level $C \in [0, 1]$.

When a student answers a question on concept $k$, the update function is:

$$M_{t+1} = \text{clamp}\Big(M_t + \Delta M, \; 5.0, \; 100.0\Big)$$

### 1.1. Case A: Correct Answer ($is\_correct = \text{True}$)

The gain is proportional to remaining headroom with diminishing returns:

$$\text{Headroom} = 100.0 - M_t$$

$$\Delta M = \text{Headroom} \times \alpha \times \left(\frac{W_{\text{diff}}}{1.4}\right) \times \mu_{\text{reasoning}} \times \tau_{\text{time}} \times (1 + \beta_{\text{streak}})$$

Where:
- $\alpha$: Base learning rate ($0.22$ for foundational $M_t < 50$, $0.16$ for advanced $M_t \ge 50$)
- $W_{\text{diff}}$: Difficulty weight:
  - $\text{Easy} = 1.0$
  - $\text{Medium} = 1.4$
  - $\text{Hard} = 1.9$
  - $\text{Advanced} = 2.5$
- $\mu_{\text{reasoning}}$: Reasoning multiplier:
  $$\mu_{\text{reasoning}} = 0.4 + 0.8 \times S_{\text{reasoning}} \quad (S_{\text{reasoning}} \in [0, 1])$$
  *A correct answer with empty reasoning ($S = 0$) receives only 40% gain, preventing lucky guesses from distorting mastery.*
- $\tau_{\text{time}}$: Response time factor:
  - $< 6\text{s}$ on Hard/Advanced: $0.65$ (flagged as rapid click/guess)
  - $10\text{s} - 90\text{s}$: $1.0$ (standard expected processing)
  - $> 180\text{s}$: $0.85$ (struggling)
- $\beta_{\text{streak}}$: Streak boost ($+5\%$ per consecutive correct, capped at $+20\%$).

### 1.2. Case B: Incorrect Answer ($is\_correct = \text{False}$)

$$\Delta M = -\Big(\text{BaseDrop} \times \gamma_{\text{misconception}} \times \rho_{\text{flaw}}\Big)$$

Where:
- $\text{BaseDrop}$: High mastery students failing an easy question suffer a larger penalty ($-14$ pts) indicating a conceptual regression, whereas novices failing hard problems suffer $-4$ pts.
- $\gamma_{\text{misconception}}$: $1.35\times$ if a specific active physical misconception was identified in the student's reasoning.
- $\rho_{\text{flaw}}$: $1.2\times$ if reasoning directly contradicted fundamental physics principles.

---

## 2. SuperMemo-2 (SM-2) Spaced Repetition Algorithm

To ensure long-term retention before board examinations, each concept is tracked with:
- $n$: Repetition count
- $EF$: Ease Factor (initial $2.5$, lower bound $1.3$)
- $I$: Interval in days
- $q$: Quality of recall ($0$ to $5$)

### SM-2 Rating Scale:
- **5**: Perfect recall with sound physical formulation.
- **4**: Correct recall after slight hesitation.
- **3**: Correct with weak or partial reasoning.
- **2**: Incorrect answer, but recalled formula once shown.
- **1**: Incorrect answer with active misconception.
- **0**: Complete blackout.

### Interval Update Equations:

$$\text{If } q \ge 3: \quad I_n = \begin{cases} 1 \text{ day} & n = 0 \\ 3 \text{ days} & n = 1 \\ \text{round}(I_{n-1} \times EF) & n > 1 \end{cases}$$

$$\text{If } q < 3: \quad n = 0, \quad I = 1 \text{ day}$$

Ease factor adjustment:

$$EF' = \max\Big(1.3, \; EF + \big(0.1 - (5 - q) \times (0.08 + (5 - q) \times 0.02)\big)\Big)$$

---

## 3. Prerequisite Traversal & Adaptive Difficulty Matching

Learnix selects the next target question automatically:
1. **Misconception Resolution**: Any concept with an active unresolved misconception is prioritized first at `easy` or `medium` difficulty.
2. **Prerequisite Gating**: If concept $B$ requires prerequisite $A$, and $M(A) < 40\%$, the engine redirects the student to reinforce $A$ before attempting $B$.
3. **Difficulty Calibration**:
   - $M < 35\% \rightarrow$ `easy`
   - $35\% \le M < 65\% \rightarrow$ `medium`
   - $65\% \le M < 85\% \rightarrow$ `hard`
   - $M \ge 85\% \rightarrow$ `advanced`
