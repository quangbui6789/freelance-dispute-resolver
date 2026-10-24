# Freelance Dispute Resolver

Intelligent Contract on GenLayer that resolves freelance / bounty disputes using live web evidence and AI consensus (Equivalence Principle).

## Features
- Create a dispute with job description and evidence links
- Resolve the dispute using web data + LLM consensus
- Returns structured result: winner, confidence, reasoning

## Deployed Contract
- Transaction: `0x4faf536ee58dbc99815d48ef848f86058861f725cf8ce0f42c2eee43536c7ffd`
- Network: GenLayer Studio

## How to use
1. Deploy the contract on [GenLayer Studio](https://studio.genlayer.com)
2. Call `create_dispute(...)` → get dispute ID
3. Call `resolve_dispute(dispute_id)`
4. Call `get_dispute(dispute_id)` to see the result

## Example
- Job: Build a simple landing page
- Client claim: Missing contact form
- Freelancer claim: Delivered as specified
