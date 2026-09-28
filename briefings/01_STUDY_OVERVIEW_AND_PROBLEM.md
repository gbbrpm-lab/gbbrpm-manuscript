# Briefing 01: Study Overview and Problem

## Official study focus

The study designs and evaluates the **Graph-Based Bounded Risk Propagation Model (GBBRPM)** for comparative node-risk prioritization across directed-network domains.

The formulation was motivated by drainage, but the final thesis focuses on the model rather than claiming a drainage-only solution.

## Thirty-second explanation

Local monitoring tells us how disturbed a component is at its location, while structural graph measures tell us where a component is important in the network. Neither alone directly answers how local disturbance and recursively accumulated network context should be combined into a bounded, traceable node-risk state. GBBRPM addresses that architectural problem using directed reachability, relation-specific susceptibility, optional transmission, current upstream risk, local disturbance, and bounded multi-source aggregation.

## The core problem

The thesis is not simply asking, “Which component is blocked?” It is asking:

> How should connected components be comparatively prioritized when current local disturbance, upstream accumulated risk, directed connectivity, and heterogeneous edge conditions all matter?

Two nodes with equal local disturbance may receive different final risk because:

- they occupy different network positions;
- their incoming edges have different susceptibility;
- their upstream nodes have different current accumulated states;
- they have different downstream reach; or
- several contributions converge at one receiver.

## Why local scores are insufficient

A local score answers: **How disturbed is this component here?**

GBBRPM answers: **Given the same network and parameterization, what is this node's current comparative risk after local and propagated context are combined?**

The second question includes the first but is not equivalent to it.

## Research questions

1. How can the model integrate local disturbance, current upstream risk, susceptibility, optional transmission, reachability, and bounded multi-source aggregation?
2. Does it preserve boundedness, monotonicity, and expected ranking behavior?
3. How sensitive, robust, and scalable is it under controlled changes?
4. Can the frozen rule be instantiated coherently in drainage, software, and electrical networks?
5. What evidence and limitations does each domain provide?

## Objectives in plain language

1. Identify the recurring mechanisms and limitations in prior approaches.
2. Formulate the bounded recursive architecture.
3. Test its mathematical and computational behavior.
4. Instantiate it in three domains without changing the core rule.
5. Compare the strength and limits of the evidence across domains.

## Primary contribution

The contribution is **architectural and integrative**, not the invention of graph propagation, susceptibility, recursion, or bounded aggregation individually.

GBBRPM contributes one explicit comparative-risk semantics that keeps these roles separate:

- topology or reachability;
- transmission or influence;
- susceptibility;
- local disturbance;
- current propagated state;
- aggregation; and
- dependence limitations.

## What the title does and does not claim

The title emphasizes design and evaluation of a bounded risk-propagation architecture across directed-network domains. “Across domains” means the same computational roles were instantiated in the tested cases. It does not mean the model is universally valid or equally predictive in every domain.

## Likely examiner questions

### “Why is drainage still prominent if the model is generic?”

Drainage supplied the original practical motivation and the richest behavioral case, including the SWMM boundary test. The formulation became generic only after separating domain-specific parameter meanings from the frozen graph update rule.

### “What exact decision does the model support?”

It supports comparative prioritization: identifying which nodes have higher modeled risk under the same graph, scenario, and parameterization. It does not prescribe a maintenance action automatically.

### “Is risk the same as failure probability?”

No. Risk is a normalized comparative index in `[0,1]`. A value of `0.70` does not mean a 70% probability of failure.

### “What is the strongest overall claim?”

The strongest claim is that GBBRPM is a coherent, bounded, traceable, and computationally tractable comparative-risk architecture on tested DAGs, with demonstrated instantiability—but unequal validation strength—across three domains.

