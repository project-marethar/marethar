import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "Marethar",
    pageTitleSuffix: " — The Setting",
    enableSPA: true,
    enablePopovers: true,
    analytics: {
      provider: "plausible",
    },
    locale: "en-US",
    baseUrl: "zeruhur.github.io/marethar_en",
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Cinzel",
        body: "Crimson Text",
        code: "IBM Plex Mono",
      },
      colors: {
        lightMode: {
          light: "#f5f0e8",
          lightgray: "#e0d8c8",
          gray: "#9a8f7e",
          darkgray: "#3a2e20",
          dark: "#1a1209",
          secondary: "#8b4513",
          tertiary: "#a0522d",
          highlight: "rgba(139, 69, 19, 0.12)",
          textHighlight: "#d4a01788",
        },
        darkMode: {
          light: "#0e0c09",
          lightgray: "#1e1a14",
          gray: "#5a4e3e",
          darkgray: "#c8b89a",
          dark: "#e8d8b8",
          secondary: "#c8860a",
          tertiary: "#a07040",
          highlight: "rgba(200, 134, 10, 0.15)",
          textHighlight: "#c8860a55",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // Comment out CustomOgImages to speed up build time
      Plugin.CustomOgImages(),
    ],
  },
}

export default config
