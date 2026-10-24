# Freelance Dispute Resolver

Intelligent Contract on GenLayer that resolves freelance / bounty disputes using live web evidence and AI consensus (Equivalence Principle).

## Deployed Contract
- **Contract Address**: `0x7C21cC383ce25CF4989ae185a38600891184D533`
- **Deploy Transaction**: `0x4faf536ee58dbc99815d48ef848f86058861f725cf8ce0f42c2eee43536c7ffd`
- **Network**: GenLayer Studio
- **Explorer**: [View on Explorer](https://explorer-studio.genlayer.com/address/0x7C21cC383ce25CF4989ae185a38600891184D533)

## Features
- Create a dispute with job description and evidence links
- Resolve the dispute using web data + LLM consensus
- Returns structured result: winner, confidence, reasoning

## How to use
1. Deploy the contract on [GenLayer Studio](https://studio.genlayer.com) (or interact with the deployed one above)
2. Call `create_dispute(...)` → get dispute ID
3. Call `resolve_dispute(dispute_id)`
4. Call `get_dispute(dispute_id)` to see the result

## Example Flow
- Job: Build a simple landing page
- Client claim: Missing contact form
- Freelancer claim: Delivered as specified
- Contract fetches evidence from URLs and reaches consensus on the winner
