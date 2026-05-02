---
title: Legitimacy Layer Interface (v1)
author: Yoshimi Nakane
version: v1.0
date: 2026-05-02
license: CC BY 4.0
---

# Legitimacy Layer Interface (v1)
Defined by Yoshimi Nakane

## Definition
A system-independent reference for evaluating the condition of human authority immediately before execution.

## Core Principle
Authority is not equivalent to formal responsibility.

Legitimacy is the condition under which human authority remains structurally valid at the moment immediately preceding execution.

## Function
The legitimacy layer interface answers a single question:

Does valid human authority still hold at the moment immediately before execution?

## Authority States

- intact
- degraded
- impaired
- stale
- conflicted
- delegated
- drifting

## Interface Role

This interface provides a portable reference state that downstream systems can consume.

Execution systems may map these states into actions such as:

- allow
- deny
- revalidation
- escalation
- proof

These mappings are not part of the legitimacy layer.

## Boundary
This interface defines whether authority is valid or degraded.

It does not prescribe execution behavior.

Execution, enforcement, and proof belong to downstream systems.
