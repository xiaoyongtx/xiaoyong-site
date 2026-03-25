# 🚀 小勇同学的个人网站

> 国企程序员的AI副业之路 - 分享AI智能体、Coze实战、副业变现和个人成长故事

![Website Status](https://img.shields.io/website?url=http://localhost:4321)
![License](https://img.shields.io/badge/license-MIT-blue)
![Astro](https://img.shields.io/badge/Astro-5.18.1-purple)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.4.0-38bdf8)

## 🌟 特色

- 🎨 **紫色主题设计**：现代、专业的视觉效果
- 📱 **响应式布局**：完美适配手机、平板、桌面端
- ⚡ **极致性能**：基于Astro静态站点生成，加载速度快
- 🤖 **AI元素**：可爱的AI机器人图标和紫色渐变设计
- 🔍 **SEO友好**：优化的Meta标签和结构化数据
- 🎯 **现代化UI**：使用Tailwind CSS构建的现代界面

## 👤 关于作者

**小勇同学**

- 🏠 老家江西，现居郑州
- 💼 国企程序员，专注AI副业
- 🤖 AI私域赚钱星球智能体首席教练
- 📈 2025年开启副业，专注AI智能体方向

## 🛠️ 技术栈

- **框架**: [Astro](https://astro.build/) - 现代化的静态站点生成器
- **样式**: [Tailwind CSS](https://tailwindcss.com/) - 实用优先的CSS框架
- **部署**: [Vercel](https://vercel.com/) - 极致的部署体验

## 📁 项目结构

```
xiaoyong-site/
├── public/                 # 静态资源
│   ├── favicon.ico         # 网站图标
│   ├── favicon.svg         # SVG图标
│   └── generate_icon.py   # 图标生成脚本
├── src/
│   ├── components/         # 组件
│   │   ├── Card.astro      # 卡片组件
│   │   ├── Footer.astro    # 页脚
│   │   └── Header.astro    # 导航栏
│   ├── layouts/            # 布局
│   │   └── Layout.astro    # 主布局
│   ├── pages/              # 页面
│   │   ├── index.astro     # 首页
│   │   ├── about.astro     # 关于页面
│   │   ├── blog/           # 博客
│   │   └── products/       # 产品展示
│   └── styles/
│       └── global.css      # 全局样式
├── astro.config.mjs        # Astro配置
├── tailwind.config.mjs     # Tailwind配置
└── package.json            # 项目依赖
```

## 🚀 快速开始

### 安装依赖

```bash
npm install
```

### 本地开发

```bash
npm run dev
```

访问 [http://localhost:4321](http://localhost:4321)

### 构建生产版本

```bash
npm run build
```

### 预览生产版本

```bash
npm run preview
```

## 📦 部署

### Vercel 部署（推荐）

1. Fork 此仓库
2. 在 [Vercel](https://vercel.com/) 导入项目
3. 即可自动部署

### 手动部署

```bash
npm run build
# 上传 dist 目录到你的服务器
```

## 🎨 自定义

### 修改颜色主题

编辑 `src/styles/global.css` 中的紫色色值：

```css
--color-primary-500: #a855f7;  /* 主色调 */
--color-primary-600: #9333ea;  /* 深色调 */
```

### 修改个人信息

- 首页：`src/pages/index.astro`
- 关于页：`src/pages/about.astro`
- Footer：`src/components/Footer.astro`

### 生成图标

如果需要重新生成网站图标：

```bash
cd public
python3 generate_icon.py
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📝 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 🔗 链接

- 🌐 网站: [https://xiaoyongtx.github.io/xiaoyong-site](https://xiaoyongtx.github.io/xiaoyong-site)
- 🐙 GitHub: [https://github.com/xiaoyongtx/xiaoyong-site](https://github.com/xiaoyongtx/xiaoyong-site)
- 📧 联系: [我是小勇同学]()

---

Made with ❤️ by 小勇同学
