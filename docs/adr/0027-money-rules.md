# ADR-0027: Money and FX rules

- Status: Approved
- Approved by: Muhammad Jariruddin, 2026-10-07 (IncomeLens ADR-018, carried forward)

## Context
Invoice, gross, fees, withholding, settlement, FX and withdrawal must not be conflated.

## Decision
Integer minor units plus ISO currency code; Decimal arithmetic with ROUND_HALF_UP set in one place; no floats. Store original and settlement amounts, FX rate, timestamp and source, platform and processor fees, and withholding. Gross minus fees minus withholding equals settlement. Every PKR figure is reproducible from stored inputs.

## Consequences
Enforced by R-24.
