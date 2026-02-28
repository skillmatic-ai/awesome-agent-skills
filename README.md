# Awesome Agent Skills [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Curated resources for building and using Agent Skills.

<div align="center">
  <a href="https://agentskills.io">
    <img src="assets/cover-image.png" alt="Agent Skills" width="90%">
  </a>
</div>

## Contents
- [What Are Agent Skills](#what-are-agent-skills)
- [Start Here](#start-here)
- [Phase 1: Learn the Fundamentals](#phase-1-learn-the-fundamentals)
- [Phase 2: Use Existing Skills](#phase-2-use-existing-skills)
- [Phase 3: Build and Integrate](#phase-3-build-and-integrate)
- [Phase 4: Benchmarks and Research](#phase-4-benchmarks-and-research)
- [Frequently Asked Questions](#frequently-asked-questions)

## What Are Agent Skills

Agent Skills are modular, standardized `SKILL.md` packages that give agents on-demand capabilities via progressive disclosure: lightweight metadata can load early, full instructions load only when relevant, and supporting resources are accessed when needed.

`agent-skills` · `ai-agents` · `skill-md` · `progressive-disclosure` · `context-management`.

## Start Here

If you are new to Agent Skills, start with these quick primers.

- [What are skills](https://agentskills.io/what-are-skills) - Guide: Beginner-friendly introduction to Agent Skills.
- [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude) - Guide: Quick start for enabling skills in Claude.

## Phase 1: Learn the Fundamentals

Concepts, comparisons, and explainers to build a solid mental model.

### Key Articles

- [Equipping agents for the real world with Agent Skills](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) - Original announcement from Anthropic Engineering.
- [Claude Skills vs MCP: Complete Guide](https://dev.to/jimquote/claude-skills-vs-mcp-complete-guide-to-token-efficient-ai-agent-architecture-4mkf) - Comparison of Agent Skills and Model Context Protocol.
- [The Great AI Agent Configuration Confusion](https://medium.com/@satinath.mondal/the-great-ai-agent-configuration-confusion-agents-md-skill-md-and-whats-next-12345) - Overview of SKILL.md, AGENTS.md, and related standards.
- [Using skills with Deep Agents](https://blog.langchain.com/using-skills-with-deep-agents/) - How frameworks apply the skills pattern.

### Video Introductions

- [Claude's new Agent Skills](https://www.youtube.com/watch?v=VRzkafNIdgI) - One-minute overview.
- [Don't Build Agents, Build Skills Instead](https://www.youtube.com/watch?v=CEvIs9y1uog) - Anthropic talk on skills as a scalable abstraction.
- [Agent Skills Explained: Why This Changes Everything](https://www.youtube.com/watch?v=Ihoxov5x66k) - Why skills matter for agent development.
- [Claude Agent Skills Tutorial and Demo](https://www.youtube.com/watch?v=mxZqEduwyFk) - Intro tutorial and hands-on demo.
- [Claude Code Skills built me an AI Agent Team](https://www.youtube.com/watch?v=OdtGN27LchE) - Extended beginner guide.

### Courses
- [Agent Skills with Anthropic](https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/) - Short course from DeepLearning.AI

## Phase 2: Use Existing Skills

Platforms that support skills today, plus ready-to-use skill catalogs.

### Supported Platforms and IDEs

- [Claude Code](https://claude.ai/code) - Platform: Anthropic's coding tool with skills support ([docs](https://code.claude.com/docs/en/skills)).
- [OpenAI Codex](https://developers.openai.com/codex/skills/) - Platform: OpenAI's CLI agent with skills support ([docs](https://developers.openai.com/codex/skills/)).
- [Gemini CLI](https://geminicli.com) - Gemini in the terminal with skills support ([docs](https://geminicli.com/docs/cli/skills/)).
- [Cursor](https://cursor.com/) - AI-powered editor with native skills integration ([docs](https://cursor.com/docs/context/skills)).
- [VS Code](https://code.visualstudio.com/) - Editor with Agent Skills support ([docs](https://code.visualstudio.com/docs/copilot/customization/agent-skills)).
- [GitHub Copilot](https://github.com/features/copilot) - Coding assistant with Agent Skills support ([docs](https://docs.github.com/copilot/concepts/agents/about-agent-skills)).
- [Mistral Vibe](https://docs.mistral.ai/mistral-vibe) - CLI coding agent with Agent Skills support by Mistral ([docs](https://docs.mistral.ai/mistral-vibe/agents-skills))
- [Manus](https://manus.im/features/agent-skills) - Autonomous AI agent, now supporting Agent Skills ([blog](https://manus.im/blog/manus-skills))
- [OpenCode](https://opencode.ai/) - AI development tool with built-in Agent Skills support ([docs](https://opencode.ai/docs/skills/)).
- [Amp](https://ampcode.com/) - AI coding assistant with Agent Skills support ([docs](https://ampcode.com/manual#agent-skills)).
- [Goose](https://block.github.io/goose/) - Open source agent framework with extensions support ([docs](https://block.github.io/goose/extensions)).
- [Letta](https://www.letta.com/) - Stateful LLM agents with memory ([docs](https://docs.letta.com/letta-code)).
- [Roo Code](https://roocode.com/) - VS Code extension and cloud agents with skills integration ([docs](https://docs.roocode.com/features/skills)).

### Ready-to-Use Skill Libraries

#### Top Picks

- [Anthropic skills](https://github.com/anthropics/skills) - Official skills catalog from Anthropic.
- [OpenAI skills](https://github.com/openai/skills) - Official skills catalog from OpenAI.
- [Microsoft skills](https://github.com/microsoft/skills) - Skills for AI coding agents working with Azure SDKs and Microsoft AI Foundry.
- [Vercel skills](https://skills.sh/vercel-labs/agent-skills) - Collection of skills reflecting best practices in web development from Vercel.
- [Supabase skills](https://github.com/supabase/agent-skills) - Agent Skills to help developers using AI agents with Supabase.
- [Hugging Face skills](https://github.com/huggingface/skills) - Community skills catalog with broad compatibility.
- [OpenClaw skills](https://www.clawhub.ai/skills) - Skills for OpenClow agents (formerly Clawd and Moltbot).

#### More Collections

- [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) - A collection of Agent Skills for context engineering (from Anthropic).
- [Orchestra-Research/AI-research-SKILLs](https://github.com/Orchestra-Research/AI-research-SKILLs) - A collection of AI/ML research and engineering skills.
- [karanb192/awesome-claude-skills](https://github.com/karanb192/awesome-claude-skills) - Curated list of Claude skills.
- [shajith003/awesome-claude-skills](https://github.com/shajith003/awesome-claude-skills) - Skill collection for specialized capabilities.
- [GuDaStudio/skills](https://github.com/GuDaStudio/skills) - Multi-agent collaboration skills.
- [DougTrajano/pydantic-ai-skills](https://github.com/DougTrajano/pydantic-ai-skills) - Pydantic AI integration skills.
- [OmidZamani/dspy-skills](https://github.com/OmidZamani/dspy-skills) - Skills for DSPy-based workflows.
- [ponderous-dustiness314/awesome-claude-skills](https://github.com/ponderous-dustiness314/awesome-claude-skills) - Document editing, data analysis, and project management skills.
- [product-on-purpose/pm-skills](https://github.com/product-on-purpose/pm-skills) - 24 plug-and-play product management skills for the full delivery lifecycle.
- [hikanner/agent-skills](https://github.com/hikanner/agent-skills) - Curated Agent Skills collection.
- [gradion-ai/freeact-skills](https://github.com/gradion-ai/freeact-skills) - Freeact skill library.

### Skill Marketplaces & directories

- [SkillsMP](https://skillsmp.com/) - Marketplace for discovering and sharing Agent Skills.
- [agentskill.sh](https://agentskill.sh) - Directory of 44k+ skills with two-layer security scanning and `/learn` installer.
- [Skillstore](https://skillstore.io/) - Curated marketplace for Agent Skills.
- [SkillsDirectory](https://www.skillsdirectory.org/) - Directory of popular Agent Skills.
- [skills.sh](https://skills.sh/) - A directory and leaderboard for Agent Skills.

## Phase 3: Build and Integrate

Guides and tools for authoring, validating, and distributing skills.

### How to Build Skills

- [A Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf?hsLang=en) - Guide: comprehensively covers how to build, test, and distribute skills.
- [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills) - Article: Step-by-step instructions for authoring skills.
- [Skills API Quickstart](https://docs.claude.com/en/api/skills-guide#creating-a-skill) - Docs: API reference for implementing skills.
- [How I Built Agent Skills for Claude Code](https://dev.to/nunc/how-i-built-agent-skills-for-claude-code-oj4) - Tutorial: Practical walkthrough for building custom skills.
- [Claude Agent Skills Tutorial](https://www.youtube.com/watch?v=fOxC44g8vig) - Video: End-to-end walkthrough with examples.

### Developer Tools

- [LangChain Multi-Agent Skills](https://docs.langchain.com/oss/python/langchain/multi-agent/skills) - Docs: Implementing skills in LangChain.
- [SkillCheck](https://github.com/agentigy/skillcheck) - Tool: Scanner for common risks in skill packages.
- [OpenSkills](https://github.com/numman-ali/openskills) - Tool: Universal loader for integrating skills with many agents.
- [LangChain Deep Agents](https://github.com/langchain-ai/deepagents) - Framework: Agent harness with a skills-oriented workflow.
- [IntentKit](https://github.com/crestalnetwork/intentkit) - Framework: Intent-driven agent building.
- [Agentica](https://github.com/wrtnlabs/agentica) - Framework: TypeScript function-calling utilities for agents.

### Reference Implementations

#### Development and Programming

- [kylehughes/the-unofficial-swift-concurrency-migration-skill](https://github.com/kylehughes/the-unofficial-swift-concurrency-migration-skill) - Skill-style guide for Swift concurrency migrations.
- [gapmiss/obsidian-plugin-skill](https://github.com/gapmiss/obsidian-plugin-skill) - Skill package for Obsidian plugin development.
- [frmoretto/stream-coding](https://github.com/frmoretto/stream-coding) - Stream-coding methodology reference.
- [remotion-dev/remotion](https://github.com/remotion-dev/remotion/tree/main/packages/skills) - Skill package that define best practices for working in Remotion projects. 

#### Integration and Automation

- [SawyerHood/dev-browser](https://github.com/SawyerHood/dev-browser) - Browser capability for agents.
- [gotalab/skillport](https://github.com/gotalab/skillport) - CLI and MCP-based skill distribution.
- [gmickel/sheets-cli](https://github.com/gmickel/sheets-cli) - Google Sheets automation via CLI.
- [fabioc-aloha/spotify-skill](https://github.com/fabioc-aloha/spotify-skill) - Spotify API integration skill.
- **[zw008/VMware-AIops](https://github.com/zw008/VMware-AIops)** - AI-powered VMware vCenter/ESXi monitoring and operations: inventory queries, health/alarms, VM lifecycle (create, delete, snapshot, clone, migrate), vSAN management, Aria Operations analytics, and scheduled log scanning. Supports Claude Code, Gemini CLI, Codex, Aider, Trae, Kimi, and MCP.

## Phase 4: Benchmarks and Research

Evaluation frameworks and deeper technical reading.

### Benchmarks and Evaluation

- [huggingface/upskill](https://github.com/huggingface/upskill) - Upskill: Generate and evaluate agent skills for code agents.
- [benchflow-ai/SkillsBench](https://github.com/benchflow-ai/SkillsBench) - Benchflow: Measuring skills performance on real workflows.

### Advanced Engineering

- [Claude Agent Skills: A First Principles Deep Dive](https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/) - Article: Detailed architecture analysis.
- [I finally CRACKED Claude Agent Skills](https://www.youtube.com/watch?v=kFpLzCVLA20) - Video: Comparison of Skills, MCP, and subagents.
- [Claude Agent Skills](https://www.youtube.com/watch?v=9XaprFRNTlc) - Video: One-hour deep dive into domain-specific usage.
- [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) - Repository: Context-engineering reference materials.
- [jakedahn/pomodoro](https://github.com/jakedahn/pomodoro) - Repository: System skill pattern reference.
- [yzfly/Mind-Cloning-Engineering](https://github.com/yzfly/Mind-Cloning-Engineering) - Repository: Techniques for building reusable skill knowledge.

### Academic Papers

- [SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks](https://arxiv.org/abs/2602.12670) (2026) - Benchmark consisting of 86 tasks across 11 domains
- [Agent Skills Enable a New Class of Realistic and Trivially Simple Prompt Injections](https://arxiv.org/abs/2510.26328) (2025) - Security analysis of skill-file prompt injection risks.
- [A survey of agent interoperability protocols](https://arxiv.org/abs/2505.02279) (2025) - Survey of MCP, Agent Cards, and related protocols.
- [Reinforcement Learning for Self-Improving Agent with Skill Library](https://arxiv.org/abs/2512.17102) (2024) - Maintaining and improving skill libraries.
- [PolySkill: Learning Generalizable Skills Through Polymorphic Abstraction](https://arxiv.org/abs/2510.15863) (2024) - Learning transferable skills via abstraction.

## Frequently Asked Questions

### What are Agent Skills

Agent Skills are modular `SKILL.md` packages that provide on-demand capabilities without loading all knowledge up front.

### How do Agent Skills differ from fine-tuning

Fine-tuning changes model weights, while skills provide runtime knowledge and workflows that you can update instantly.

### What is the difference between Agent Skills and MCP

Agent Skills focus on workflows and capabilities, while MCP focuses on secure, structured data and tool access.

### How do I create my first Agent Skill

See the [How to Build Skills](#how-to-build-skills) section for a step-by-step authoring guide.

### Which AI platforms support Agent Skills

Support varies by platform, but major tools include Claude (Claude.ai and Claude Code), OpenAI Codex, GitHub Copilot, Cursor, VS Code, and more.

### Can I use Agent Skills with ChatGPT or other LLMs

If a platform does not support the format natively, you can often integrate skills via a loader or by adapting the `SKILL.md` instructions into that platform's prompt workflow.

### Are Agent Skills secure

Treat skills like code: review them before using, avoid installing from untrusted sources, and prefer audited skill libraries.

### How do I share Agent Skills with my team

The most common approach is to version skills in Git (in a shared repo) and let your supported tools discover them from a standard directory.

## Contributing

Please read our [contribution guidelines](contributing.md) before submitting changes.
