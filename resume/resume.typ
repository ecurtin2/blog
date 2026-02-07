// Resume template - reads from data/profile.toml
#let profile = toml("/data/profile.toml")
#let p = profile.personal
#let bio = profile.bio
#let skills = profile.skills

// Color palette (matches blog theme)
#let teal = rgb("#037171")
#let green = rgb("#2a7f62")
#let darkgreen = rgb("#03312e")
#let blue = rgb("#0066BB")
#let fg = rgb("#1d1d1d")
#let light-gray = rgb("#666666")

#set document(
  title: [#p.name - Resume],
  author: p.name,
)

#set page(
  paper: "us-letter",
  margin: (x: 0.75in, y: 0.75in),
)

#set text(
  font: "DejaVu Sans",
  size: 10pt,
  fill: fg,
)

#set par(
  justify: true,
  leading: 0.65em,
)

// Link styling
#show link: it => text(fill: blue, it)

// Strong text styling
#show strong: it => text(fill: darkgreen, weight: "semibold", it)

// Heading styles
#show heading.where(level: 1): it => [
  #set text(size: 20pt, weight: "bold", fill: teal)
  #it.body
]

#show heading.where(level: 2): it => [
  #v(0.6em)
  #set text(size: 11pt, weight: "semibold", fill: green)
  #upper(it.body)
  #v(-0.4em)
  #line(length: 100%, stroke: 1.5pt + green.lighten(70%))
  #v(0.3em)
]

#show heading.where(level: 3): it => [
  #set text(size: 10pt, weight: "semibold", fill: darkgreen)
  #it.body
]

// Name and contact header
#align(center)[
  #text(size: 22pt, weight: "bold", fill: teal)[#p.name]
  #v(-0.4em)
  #text(size: 10.5pt, style: "italic", fill: light-gray)[#bio.tagline]
  #v(0.3em)
  #text(size: 9pt, fill: fg)[
    #p.location #h(0.5em) | #h(0.5em)
    #link("mailto:" + p.email)[#p.email] #h(0.5em) | #h(0.5em)
    #p.phone #h(0.5em) | #h(0.5em)
    #link(p.github)[github.com/ecurtin2]
  ]
]

#v(0.6em)
#text(size: 10pt)[#bio.summary]

== Skills

#let skill-line(label, items) = [
  *#label:* #items.join(", ")
]

#skill-line("Strong", skills.strong) \
#skill-line("Proficient", skills.proficient) \
#skill-line("Familiar", skills.familiar) \
#skill-line("Interested in", skills.interested_in)

== Experience

#for job in profile.experience [
  #let start_year = job.start_date.slice(0, 4)
  #let end_year = if job.end_date == "present" { "Present" } else { job.end_date.slice(0, 4) }
  
  === #job.title – #job.company
  #text(size: 9pt, fill: light-gray)[#start_year – #end_year, #job.location]
  
  #for highlight in job.highlights [
    - #highlight
  ]
  #v(0.3em)
]

== Education

#for edu in profile.education [
  === #edu.degree, #edu.institution
  #if "focus" in edu [
    Focus: #edu.focus \
  ]
  #if "thesis" in edu [
    Thesis: #edu.thesis#if "minor" in edu [. #edu.minor Minor.]
  ]
  #if "technologies" in edu [
    Technologies: #edu.technologies.join(", ")
  ]
  #v(0.25em)
]

== Publications

#for (i, pub) in profile.publications.enumerate() {
  let vol = if "volume" in pub { ", vol. " + pub.volume } else { "" }
  let iss = if "issue" in pub { ", no. " + pub.issue } else { "" }
  let pg = if "page" in pub { ", p. " + pub.page } else { "" }
  let pgs = if "pages" in pub { ", pp. " + pub.pages } else { "" }
  
  [#(i + 1). #pub.authors.join(", "), "#pub.title," #emph(pub.venue)#vol#iss#pg#pgs, #pub.year.]
  parbreak()
}

== Projects

#for proj in profile.projects [
  - #link(proj.url)[*#proj.name*]: #proj.description
]
