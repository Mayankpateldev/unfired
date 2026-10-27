# Runway and income: make uncertainty visible

Begin with a scenario, not a promise. This worksheet is a simplified planning aid; it does not calculate taxes, benefit eligibility, debt strategy, inflation, or investment decisions.

## Make a conservative snapshot

1. Record cash available for living costs today. Keep retirement assets and unreceived severance out of this figure unless you deliberately model them separately.
2. Write down essential monthly costs: housing, food, utilities, transport, insurance, minimum obligations, and dependants' needs.
3. List dependable monthly income separately. Irregular or possible income belongs in a second scenario.
4. Choose a reserve you do not want to spend in this scenario.
5. Recalculate when payments, costs, or work change.

```bash
python3 tools/unfired.py runway --cash 9000 --reserve 1000 --monthly-costs 2500 --monthly-income 500
```

The example leaves 8,000 usable cash and a 2,000 monthly gap: **4.0 months**, assuming constant costs and income. Zero or negative gap means this particular model shows no depletion; it does not mean permanent financial security. Use one currency throughout. The tool makes no currency conversion and cannot account for cash-flow timing within a month.

## Three scenarios

| Scenario | Income assumption | Question |
| --- | --- | --- |
| Conservative | Confirmed recurring income only | What must change if nothing new arrives? |
| Bridge | A realistic short contract, with costs and taxes considered separately | Does it buy time without consuming the whole week? |
| Recovery | A new role or repeat clients | What should be rebuilt before taking on more commitments? |

Use [budget.csv](../templates/budget.csv) privately. Do not post balances or benefit identifiers in issues. Local financial counselling, government benefits services, or a qualified adviser can help with decisions this model cannot cover.

## Choose an income track

- **Employment:** pick two target role types, seek warm introductions, and keep a manageable application cadence.
- **Freelance:** offer one bounded deliverable, such as cleaning a client's authorized CSV export. Specify input, output, price, revision limit, and handover in writing.
- **Services around open source:** installation, migration, training, accessibility review, or support. Keep the public source available while charging for your time.
- **Cooperative/team:** agree on ownership, compensation, decision-making, and maintenance before making customer promises.

Consult the relevant agency about how freelance work, business activity, or earnings affect benefit reporting. Do not assume unpaid project work or small invoices are exempt.

## A week you can actually repeat

Start with three focused sessions per day at most: one income task, one relationship task, and one learning/building task. Reduce this if caring responsibilities, health, or stress require it. At week's end ask: what produced useful conversations, completed work, or relief? Cut one activity that only produced anxiety.
