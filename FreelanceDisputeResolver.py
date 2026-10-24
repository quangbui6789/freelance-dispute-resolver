# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *
import json


class FreelanceDisputeResolver(gl.Contract):
    # Chỉ dùng str
    data: str
    counter: str

    def __init__(self):
        self.data = "{}"
        self.counter = "0"

    @gl.public.write
    def create_dispute(
        self,
        job_description: str,
        deliverable_url: str,
        evidence_url: str,
        client_claim: str,
        freelancer_claim: str,
    ) -> str:
        disputes = json.loads(self.data)
        did = int(self.counter)

        disputes[str(did)] = {
            "job": job_description,
            "deliverable": deliverable_url,
            "evidence": evidence_url,
            "client": client_claim,
            "freelancer": freelancer_claim,
            "status": "open",
            "winner": "",
            "confidence": "0",
            "reasoning": "",
        }

        self.data = json.dumps(disputes)
        self.counter = str(did + 1)
        return str(did)

    @gl.public.write
    def resolve_dispute(self, dispute_id: str) -> None:
        disputes = json.loads(self.data)
        if dispute_id not in disputes:
            raise ValueError("Not found")

        d = disputes[dispute_id]
        if d["status"] != "open":
            raise ValueError("Already resolved")

        def get_evidence() -> str:
            text = ""
            for url in [d["deliverable"], d["evidence"]]:
                if url:
                    try:
                        content = gl.nondet.web.render(url, mode="text")
                        text += content[:4000] + "\n"
                    except:
                        text += "Failed\n"
            return text

        def judge() -> str:
            evidence = get_evidence()
            prompt = f"""Resolve this freelance dispute.

Job: {d['job']}
Client: {d['client']}
Freelancer: {d['freelancer']}
Evidence: {evidence}

Return only JSON:
{{"winner":"client|freelancer|split","confidence":"80","reasoning":"short reason"}}
"""
            return gl.exec_prompt(prompt)

        result = gl.eq_principle.prompt_non_comparative(
            judge,
            task="Resolve dispute",
            criteria="Must be valid JSON with winner, confidence, reasoning"
        )

        try:
            res = json.loads(result) if isinstance(result, str) else result
            d["winner"] = str(res.get("winner", "split"))
            d["confidence"] = str(res.get("confidence", "50"))
            d["reasoning"] = str(res.get("reasoning", ""))[:800]
        except:
            d["winner"] = "split"
            d["confidence"] = "50"
            d["reasoning"] = "Parse error"

        d["status"] = "resolved"
        disputes[dispute_id] = d
        self.data = json.dumps(disputes)

    @gl.public.view
    def get_dispute(self, dispute_id: str) -> str:
        disputes = json.loads(self.data)
        return json.dumps(disputes.get(dispute_id, {}))

    @gl.public.view
    def get_counter(self) -> str:
        return self.counter
