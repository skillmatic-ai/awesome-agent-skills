# 🎯 Awesome Agent Skills [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<div align="center">
  <img src="assets/cover-image.png" alt="Awesome Agent Skills - The definitive resource for Agent Skills" width="100%">
</div>

<br>

## 💡 What Are Agent Skills?

**Agent Skills** mark a fundamental shift from monolithic AI systems to composable agent architectures. Rather than embedding capabilities through expensive fine-tuning or bloating context windows with static documentation, skills provide **modular, on-demand knowledge injection** through standardized `SKILL.md` packages.

### The Architecture

**Progressive Disclosure at Scale**: Skills leverage a three-tier context management strategy:
1. **Discovery** (~50 tokens): Lightweight metadata (name + description) loads at startup
2. **Activation** (~2-5K tokens): Full `SKILL.md` instructions load when task-relevant  
3. **Execution**: Referenced scripts and resources accessed dynamically

This architecture delivers:
- 🧠 **Infinite capability scaling** - No context window trade-offs
- ⚡ **Sub-second skill loading** - Zero startup latency penalty
- 🔄 **Cross-platform portability** - Write once, deploy to any compatible agent
- 📦 **Frictionless distribution** - Share via Git, install like packages

### The Revolution

**From specialized agents to universal platforms**: Instead of building separate coding agents, research agents, and analysis agents, the industry is converging on **general-purpose agents with skill libraries**. One agent. Unlimited specializations. Dynamic composition.

> "We used to think agents in different domains will look very different. The agent underneath is actually more universal than we thought."  
> — *Barry Zhang, Anthropic Research*

**The open standard advantage**: Major platforms (OpenAI, GitHub, Microsoft, Cursor) have adopted the Agent Skills specification, creating **network effects**: every skill you create works across the entire ecosystem. This is the npm moment for AI agents.

### 🏷️ Key Topics

`agent-skills` · `ai-agents` · `llm` · `claude` · `anthropic` · `skill-md` · `progressive-disclosure` · `context-management` · `ai-development` · `mcp` · `agent-architecture` · `agentic-ai` · `automation` · `productivity`

👉 **New to Agent Skills?** Start here: [agentskills.io](https://agentskills.io)

## 📚 What's Inside?

- [Start Here](#-start-here) - Introduction to the concepts
- [Phase 1: Learn the Fundamentals](#-phase-1-learn-the-fundamentals) - Articles and videos to get started
- [Phase 2: Use Existing Skills](#-phase-2-use-existing-skills) - Platforms and ready-to-use libraries
- [Phase 3: Build & Integrate](#-phase-3-build--integrate) - Create your own skills and tools
- [Phase 4: Master & Research](#-phase-4-master--research) - Advanced engineering and theory
- [Frequently Asked Questions](#-frequently-asked-questions) - Common questions answered
- [Community & Contributing](#-community--contributing) - Join the movement

## 🏁 Start Here

**New to Agent Skills?** These resources will take you from zero to understanding the core concepts in minutes.

### 🎓 Getting Started

- [What are skills?](https://agentskills.io/what-are-skills) - Perfect introduction for beginners
- [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude) - Quick start guide
- [Agent Skills Review](https://www.youtube.com/watch?v=tGpeWM7gOlA) - 25-second feature highlight

## 🎓 Phase 1: Learn the Fundamentals

**Understand the "Why" and "How".** Before diving into code, grasp the architectural shift and best practices.

### 📰 Key Concepts & Articles

- [Equipping agents for the real world with Agent Skills](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) - The original announcement from Anthropic Engineering
- [Using skills with Deep Agents](https://blog.langchain.com/using-skills-with-deep-agents/) - How generalist agents use skills for efficiency
- [Agent Skills Explained: Why This Changes Everything](https://www.youtube.com/watch?v=Ihoxov5x66k) - 17-minute analysis of why Skills matter for AI development
- [Claude Skills vs MCP: Complete Guide](https://dev.to/jimquote/claude-skills-vs-mcp-complete-guide-to-token-efficient-ai-agent-architecture-4mkf) - Comparison of Skills and Model Context Protocol architectures
- [The Great AI Agent Configuration Confusion](https://medium.com/@satinath.mondal/the-great-ai-agent-configuration-confusion-agents-md-skill-md-and-whats-next-12345) - Understanding configuration standards (SKILL.md, AGENTS.md)

### 🎬 Video Introductions
- [Don’t Build Agents, Build Skills Instead (Anthropic)](https://www.youtube.com/watch?v=CEvIs9y1uog) - Why “skills” are the scalable abstraction for agent capability
- [A better way to build agents? Claude Agent Skills Tutorial + Demo](https://www.youtube.com/watch?v=mxZqEduwyFk) - 11-minute intro: Is Agent Skills the next big standard after MCP?
- [Claude's new 'Agent Skills'](https://www.youtube.com/watch?v=VRzkafNIdgI) - 1-minute quick overview - installable "mini-brains"
- [Claude Code Skills just Built me an AI Agent Team (2026 Guide)](https://www.youtube.com/watch?v=OdtGN27LchE) - 27-minute beginner guide to building general AI agents

## 🛠️ Phase 2: Use Existing Skills

**Experience the power.** Don't build from scratch—leverage the ecosystem of platforms and pre-built libraries.

### 🎨 Supported Platforms & IDEs

**Where can you use Agent Skills today?**

- [Cursor](https://cursor.com/) - AI-powered code editor with native skills integration ([docs](https://cursor.com/docs/context/skills))
- [Claude Code](https://claude.ai/code) - Anthropic's coding tool with first-class skills support ([docs](https://code.claude.com/docs/en/skills))
- [GitHub Copilot](https://github.com/features/copilot) - GitHub's AI coding assistant with Agent Skills support ([docs](https://docs.github.com/copilot/concepts/agents/about-agent-skills))
- [VS Code](https://code.visualstudio.com/) - Microsoft's editor with Agent Skills in Insiders build ([docs](https://code.visualstudio.com/docs/copilot/customization/agent-skills))
- [OpenAI Codex](https://developers.openai.com/codex/skills/) - OpenAI's CLI agent with Agent Skills support ([docs](https://developers.openai.com/codex/skills/))
- [OpenCode](https://opencode.ai/) - AI development tool with built-in Agent Skills support ([docs](https://opencode.ai/docs/skills/))
- [Amp](https://ampcode.com/) - Next-gen AI coding assistant ([docs](https://ampcode.com/manual#agent-skills))
- [Goose](https://block.github.io/goose/) - Open source AI agent framework ([docs](https://block.github.io/goose/extensions))
- [Letta](https://www.letta.com/) - Build stateful LLM agents with memory ([docs](https://docs.letta.com/letta-code))
- [Gemini CLI](https://geminicli.com) - Google's solution for bringing Gemini into the terminal ([docs](https://geminicli.com/docs/cli/skills/))

### 📦 Ready-to-Use Skill Libraries

**Tap into battle-tested capabilities.**

#### 🔥 Top Picks
- <a href="https://github.com/anthropics/skills" target="_blank" rel="noopener noreferrer">Official collection from Anthropic (document editing, data analysis, etc.)</a>
- <a href="https://github.com/openai/skills" target="_blank" rel="noopener noreferrer">Official collection from OpenAI (Codex skills catalog)</a>
- <a href="https://github.com/huggingface/skills" target="_blank" rel="noopener noreferrer">Official collection from Hugging Face (compatible with Claude, Codex, Gemini)</a>
- <a href="https://github.com/karanb192/awesome-claude-skills" target="_blank" rel="noopener noreferrer">50+ verified skills for Claude Code and Claude.ai</a>
- <a href="https://github.com/shajith003/awesome-claude-skills" target="_blank" rel="noopener noreferrer">Skills for specialized capabilities</a>

#### 📂 More Collections
- <a href="https://github.com/GuDaStudio/skills" target="_blank" rel="noopener noreferrer">Multi-agent collaboration skills</a>
- <a href="https://github.com/DougTrajano/pydantic-ai-skills" target="_blank" rel="noopener noreferrer">Pydantic AI integration</a>
- <a href="https://github.com/OmidZamani/dspy-skills" target="_blank" rel="noopener noreferrer">Skills for DSPy framework</a>
- <a href="https://github.com/ponderous-dustiness314/awesome-claude-skills" target="_blank" rel="noopener noreferrer">Document editing, data analysis, and project management</a>
- <a href="https://github.com/hikanner/agent-skills" target="_blank" rel="noopener noreferrer">Curated Claude Agent Skills collection</a>
- <a href="https://github.com/gradion-ai/freeact-skills" target="_blank" rel="noopener noreferrer">Freeact agent library skills</a>

### 🏪 Skill Marketplaces
- [SkillsMP](https://skillsmp.com/) - Agent Skills marketplace for Claude Code/Codex (discover, install, and share skills)
- [Skillstore](https://skillstore.io/) - Curated, security-audited Agent Skills marketplace for Claude Code and Codex

## 🏗️ Phase 3: Build & Integrate

**Create your own.** Learn to author `SKILL.md` files and integrate them into your workflows.

### 📝 How to Build Skills

- [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills) - Step-by-step authoring guide
- [Skills API Quickstart](https://docs.claude.com/en/api/skills-guide#creating-a-skill) - Technical documentation
- [How I Built Agent Skills for Claude Code](https://dev.to/nunc/how-i-built-agent-skills-for-claude-code-oj4) - 8-minute tutorial on building custom Agent Skills from scratch
- [Claude Agent Skills Tutorial](https://www.youtube.com/watch?v=fOxC44g8vig) - Comprehensive implementation tutorial with SKILL.md format

### 🔧 Developer Tools

**Frameworks and utilities for building and loading skills.**

- [LangChain Multi-Agent Skills](https://docs.langchain.com/oss/python/langchain/multi-agent/skills) - Official documentation on implementing the skills pattern in LangChain
- [SkillCheck](https://github.com/agentigy/skillcheck) - Security scanner for SKILL.md files - detect vulnerabilities before production
- [OpenSkills](https://github.com/numman-ali/openskills) - Universal skills loader for any AI agent
- [LangChain Deep Agents](https://github.com/langchain-ai/deepagents) - Open source agent harness with skills support
- [IntentKit](https://github.com/crestalnetwork/intentkit) - Framework for intent-driven AI agents
- [Agentica](https://github.com/wrtnlabs/agentica) - TypeScript AI function calling framework

### 💡 Reference Implementations (By Category)

**Learn from examples.**

#### Development & Programming
- <a href="https://github.com/kylehughes/the-unofficial-swift-concurrency-migration-skill" target="_blank" rel="noopener noreferrer">Swift Concurrency Migration guide</a>
- <a href="https://github.com/gapmiss/obsidian-plugin-skill" target="_blank" rel="noopener noreferrer">Obsidian.md plugin development</a>
- <a href="https://github.com/frmoretto/stream-coding" target="_blank" rel="noopener noreferrer">Stream Coding methodology</a>

#### Integration & Automation
- <a href="https://github.com/SawyerHood/dev-browser" target="_blank" rel="noopener noreferrer">Web browser capability for agents</a>
- <a href="https://github.com/gotalab/skillport" target="_blank" rel="noopener noreferrer">Skills for any agent via CLI or MCP</a>
- <a href="https://github.com/gmickel/sheets-cli" target="_blank" rel="noopener noreferrer">Google Sheets CLI automation</a>
- <a href="https://github.com/fabioc-aloha/spotify-skill" target="_blank" rel="noopener noreferrer">Spotify API integration</a>

## 🔬 Phase 4: Benchmarks & Research

**Deepen your expertise.** Explore evaluations, security implications, and academic research.

### 📏 Benchmarks & Evaluation
- <a href="https://github.com/benchflow-ai/SkillsBench" target="_blank" rel="noopener noreferrer">SkillsBench</a> - Benchmark/evaluation framework for measuring Agent Skills performance on real workflows

### 🧠 Advanced Engineering

- [Claude Agent Skills: A First Principles Deep Dive](https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/) - Comprehensive analysis of the internal architecture
- [I finally CRACKED Claude Agent Skills](https://www.youtube.com/watch?v=kFpLzCVLA20) - Engineering breakdown: Skills vs MCP vs Subagents
- [Claude Agent Skills](https://www.youtube.com/watch?v=9XaprFRNTlc) - 1-hour deep dive into domain-specific AI expertise
- <a href="https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering" target="_blank" rel="noopener noreferrer">Context engineering techniques</a>
- <a href="https://github.com/jakedahn/pomodoro" target="_blank" rel="noopener noreferrer">System Skill Pattern (skills that remember & improve)</a>
- <a href="https://github.com/yzfly/Mind-Cloning-Engineering" target="_blank" rel="noopener noreferrer">Mind cloning with LLM skills</a>

### 🛡️ Academic Papers

- [Agent Skills Enable a New Class of Realistic and Trivially Simple Prompt Injections](https://arxiv.org/abs/2510.26328) (2025) - Security analysis showing vulnerabilities in Agent Skills markdown files
- [A survey of agent interoperability protocols](https://arxiv.org/abs/2505.02279) (2025) - Comprehensive look at MCP, Agent Cards, and more
- [Reinforcement Learning for Self-Improving Agent with Skill Library](https://arxiv.org/abs/2512.17102) (2024) - Framework for agents to build and maintain skill libraries
- [PolySkill: Learning Generalizable Skills Through Polymorphic Abstraction](https://arxiv.org/abs/2510.15863) (2024) - Learning generalizable skills through polymorphic abstraction

## ❓ Frequently Asked Questions

### What are Agent Skills?

Agent Skills are modular, standardized `SKILL.md` packages that provide AI agents with on-demand capabilities. Instead of fine-tuning models or bloating context windows, skills enable **progressive disclosure**: lightweight metadata loads at startup (~50 tokens), full instructions activate when needed (~2-5K tokens), and resources load dynamically during execution.

### How do Agent Skills differ from fine-tuning?

Fine-tuning modifies model weights permanently (expensive, inflexible), while Agent Skills provide **runtime knowledge injection** that's instantly updatable, shareable across platforms, and requires zero retraining. Update a skill once, and every agent using it benefits immediately.

### What's the difference between Agent Skills and MCP (Model Context Protocol)?

**Agent Skills** focus on **capabilities and workflows** (how to do X), while **MCP** focuses on **data access** (connecting to APIs, databases). They're complementary: use MCP to connect to external data sources, use Skills to teach agents how to process that data. Many developers use both together.

### How do I create my first Agent Skill?

1. Create a `SKILL.md` file with YAML frontmatter (name, description)
2. Write clear instructions in markdown (what, when, how)
3. Add optional `scripts/` folder for code references
4. Place in `.github/skills/` or `.claude/skills/` directory
5. Test with compatible platforms (Claude Code, Cursor, GitHub Copilot)

👉 Full guide: [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)

### Which AI platforms support Agent Skills?

Major platforms with native support include: **Claude** (Claude.ai, Claude Code), **OpenAI** (Codex CLI), **GitHub Copilot**, **Cursor**, **VS Code Insiders**, **OpenCode**, **Amp**, **Letta**, and **Goose**. The ecosystem is rapidly expanding as more platforms adopt the open standard.

### Can I use Agent Skills with ChatGPT or other LLMs?

While ChatGPT doesn't natively support the Agent Skills format, you can use universal loaders like [openskills](https://github.com/numman-ali/openskills) to integrate skills with any LLM platform. The skills specification is open and platform-agnostic by design.

### Are Agent Skills secure?

Agent Skills introduce new security considerations. Since skills can execute code and access files, always **review skills before installation** from untrusted sources. Use tools like [skillcheck](https://github.com/agentigy/skillcheck) to scan for vulnerabilities. Research shows potential for prompt injection attacks ([arxiv.org/abs/2510.26328](https://arxiv.org/abs/2510.26328)), so treat skills like code packages—audit before trusting.

### How do I share Agent Skills with my team?

**Option 1**: Commit to your repository's `.github/skills/` or `.claude/skills/` directory—agents automatically discover them.  
**Option 2**: Publish to GitHub as a standalone repo (e.g., `my-org/data-analysis-skill`)—others can reference or clone.  
**Option 3**: Use [skillport](https://github.com/gotalab/skillport) or [agent-skills-mcp](https://github.com/DiscreteTom/agent-skills-mcp) for cross-platform distribution.

### What makes a good Agent Skill?

**Best practices:**
- **Single responsibility** - One clear capability per skill
- **Progressive detail** - Brief metadata, detailed instructions, extensive resources
- **Context-aware** - Include when/why to use (not just how)
- **Testable** - Provide example inputs/outputs
- **Discoverable** - Descriptive names and rich descriptions

### When should I use Agent Skills vs custom tools/functions?

Use **Agent Skills** when:
- Capabilities need to work across multiple platforms
- Instructions are complex multi-step workflows
- You want version control and collaborative editing
- Knowledge needs frequent updates

Use **custom tools/functions** when:
- Platform-specific integration required (e.g., API-specific features)
- Real-time data access needed
- Computational logic can't be expressed as instructions

### Can Agent Skills call other Agent Skills?

Yes! Skills can reference other skills in their instructions, enabling **skill composition**. This allows building complex capabilities from simple, reusable building blocks. Some platforms also support **skill libraries** where skills automatically discover and leverage related capabilities.

### How do Agent Skills impact token usage?

**Dramatically reduce it.** Traditional approaches load all documentation upfront (10K-100K tokens), while skills load only what's needed (50 tokens metadata + 2-5K when activated). For agents managing 50+ capabilities, this means **90%+ token reduction** during idle time.

### Are Agent Skills just for coding tasks?

No—Agent Skills work for any domain: **data analysis**, **content creation**, **project management**, **research**, **security operations**, **automation**, and more. The format is domain-agnostic. Think of them as "packages for knowledge" rather than "packages for code."

### Where can I find production-ready Agent Skills?

Start with:
- [anthropics/skills](https://github.com/anthropics/skills) - Official Anthropic collection
- [karanb192/awesome-claude-skills](https://github.com/karanb192/awesome-claude-skills) - 50+ verified skills
- This repository's [Ready-to-Use Skills](#-ready-to-use-skills) section

### How often should I update my Agent Skills?

Update skills whenever:
- Platform APIs or tools change
- Better approaches emerge
- Team workflows evolve
- User feedback reveals gaps

**Pro tip**: Add version numbers and changelogs to your skills for better tracking.

## 💬 Join the Community

**You're not alone in this.** Join thousands of developers pioneering the future of AI agents - share breakthroughs, debug challenges, and shape the standards.

- 💭 [Agent Skills GitHub Discussions](https://github.com/agentskills/agentskills/discussions) - Official specification discussions
- 🐛 [Anthropic Skills GitHub Issues](https://github.com/anthropics/skills/issues) - Report issues and request features
- ⭐ **Star this repo** to stay updated with the latest resources!

## 🤝 Contributing

**Shape the ecosystem.** This is a community-driven resource - your contributions help thousands of developers discover and build better agent systems.

- Add new skills, tools, or articles
- Improve documentation
- Fix broken links
- Suggest new sections

Please read our [contribution guidelines](CONTRIBUTING.md) before submitting.

---

<div align="center">

**Found this useful? Give it a ⭐ and share it with others!**

*Built with ❤️ by the Agent Skills community*

</div>
