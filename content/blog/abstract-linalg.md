---
author: Evan Curtin
date: 2018-03-03T10:52:12-05:00
slug: abstract-linalg
tags:
- Python
- math
title: Abstract linear algebra in Python
desc: Hey dude
draft: False
---

<div class="notebook-content">
<style type="text/css">/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI escape sequences */
/* The color values are a mix of
   http://www.xcolors.net/dl/baskerville-ivorylight and
   http://www.xcolors.net/dl/euphrasia */
.ansi-black-fg {
  color: #3E424D;
}
.ansi-black-bg {
  background-color: #3E424D;
}
.ansi-black-intense-fg {
  color: #282C36;
}
.ansi-black-intense-bg {
  background-color: #282C36;
}
.ansi-red-fg {
  color: #E75C58;
}
.ansi-red-bg {
  background-color: #E75C58;
}
.ansi-red-intense-fg {
  color: #B22B31;
}
.ansi-red-intense-bg {
  background-color: #B22B31;
}
.ansi-green-fg {
  color: #00A250;
}
.ansi-green-bg {
  background-color: #00A250;
}
.ansi-green-intense-fg {
  color: #007427;
}
.ansi-green-intense-bg {
  background-color: #007427;
}
.ansi-yellow-fg {
  color: #DDB62B;
}
.ansi-yellow-bg {
  background-color: #DDB62B;
}
.ansi-yellow-intense-fg {
  color: #B27D12;
}
.ansi-yellow-intense-bg {
  background-color: #B27D12;
}
.ansi-blue-fg {
  color: #208FFB;
}
.ansi-blue-bg {
  background-color: #208FFB;
}
.ansi-blue-intense-fg {
  color: #0065CA;
}
.ansi-blue-intense-bg {
  background-color: #0065CA;
}
.ansi-magenta-fg {
  color: #D160C4;
}
.ansi-magenta-bg {
  background-color: #D160C4;
}
.ansi-magenta-intense-fg {
  color: #A03196;
}
.ansi-magenta-intense-bg {
  background-color: #A03196;
}
.ansi-cyan-fg {
  color: #60C6C8;
}
.ansi-cyan-bg {
  background-color: #60C6C8;
}
.ansi-cyan-intense-fg {
  color: #258F8F;
}
.ansi-cyan-intense-bg {
  background-color: #258F8F;
}
.ansi-white-fg {
  color: #C5C1B4;
}
.ansi-white-bg {
  background-color: #C5C1B4;
}
.ansi-white-intense-fg {
  color: #A1A6B2;
}
.ansi-white-intense-bg {
  background-color: #A1A6B2;
}
.ansi-default-inverse-fg {
  color: #FFFFFF;
}
.ansi-default-inverse-bg {
  background-color: #000000;
}
.ansi-bold {
  font-weight: bold;
}
.ansi-underline {
  text-decoration: underline;
}
/* The following styles are deprecated an will be removed in a future version */
.ansibold {
  font-weight: bold;
}
.ansi-inverse {
  outline: 0.5px dotted;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  position: relative;
  overflow: visible;
}
div.cell:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: transparent;
}
div.cell.jupyter-soft-selected {
  border-left-color: #E3F2FD;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #E3F2FD;
  border-right-width: 1px;
  background: #E3F2FD;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected,
div.cell.selected.jupyter-soft-selected {
  border-color: #ababab;
}
div.cell.selected:before,
div.cell.selected.jupyter-soft-selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #42A5F5;
}
@media print {
  div.cell.selected,
  div.cell.selected.jupyter-soft-selected {
    border-color: transparent;
  }
}
.edit_mode div.cell.selected {
  border-color: #66BB6A;
}
.edit_mode div.cell.selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #66BB6A;
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  min-width: 0;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303F9F;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  /* Note that this should set vertical padding only, since CodeMirror assumes
       that horizontal padding will be set on CodeMirror pre */
  padding: 0.4em 0;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. This sets horizontal padding only,
    use .CodeMirror-lines for vertical */
  padding: 0 0.4em;
  border: 0;
  border-radius: 0;
}
.CodeMirror-cursor {
  border-left: 1.4px solid black;
}
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .CodeMirror-cursor {
    border-left: 2px solid black;
  }
}
@media screen and (min-width: 4320px) {
  .CodeMirror-cursor {
    border-left: 4px solid black;
  }
}
/*

Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme

*/
.highlight-base {
  color: #000;
}
.highlight-variable {
  color: #000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-header {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-header {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000;
  box-shadow: inset 0 0 1px #000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #D84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area 
div.output_area 
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
div.output_area .mglyph > img {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
div.output_area pre {
  margin: 0;
  padding: 1px 0 1px 0;
  border: 0;
  vertical-align: baseline;
  color: black;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000;
  /* any extras will just be numbers: */
}



.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}






.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul:not(.list-inline),
.rendered_html ol:not(.list-inline) {
  padding-left: 2em;
}








.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}





.rendered_html pre,




.rendered_html tr,
.rendered_html th,


.rendered_html tbody tr:nth-child(odd) {
  background: #f5f5f5;
}
.rendered_html tbody tr:hover {
  background: rgba(66, 165, 245, 0.2);
}
.rendered_html * + table {
  margin-top: 1em;
}

.rendered_html * + p {
  margin-top: 1em;
}

.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,

.rendered_html img.unconfined,


.rendered_html * + .alert {
  margin-top: 1em;
}
[dir="rtl"] 
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered 
.text_cell.rendered .rendered_html tr,
.text_cell.rendered .rendered_html th,
.text_cell.rendered 
.text_cell.unrendered .text_cell_render {
  display: none;
}
.text_cell .dropzone .input_area {
  border: 2px dashed #bababa;
  margin: -1px;
}
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-header-1 {
  font-size: 185.7%;
}
.cm-header-2 {
  font-size: 157.1%;
}
.cm-header-3 {
  font-size: 128.6%;
}
.cm-header-4 {
  font-size: 110%;
}
.cm-header-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-header-6 {
  font-size: 100%;
  font-style: italic;
}
</style>
<style type="text/css">.highlight-ipynb .hll { background-color: #ffffcc }
.highlight-ipynb  { background: #f8f8f8; }
.highlight-ipynb .c { color: #408080; font-style: italic } /* Comment */
.highlight-ipynb .err { border: 1px solid #FF0000 } /* Error */
.highlight-ipynb .k { color: #008000; font-weight: bold } /* Keyword */
.highlight-ipynb .o { color: #666666 } /* Operator */
.highlight-ipynb .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight-ipynb .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight-ipynb .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight-ipynb .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight-ipynb .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight-ipynb .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight-ipynb .gd { color: #A00000 } /* Generic.Deleted */
.highlight-ipynb .ge { font-style: italic } /* Generic.Emph */
.highlight-ipynb .gr { color: #FF0000 } /* Generic.Error */
.highlight-ipynb .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight-ipynb .gi { color: #00A000 } /* Generic.Inserted */
.highlight-ipynb .go { color: #888888 } /* Generic.Output */
.highlight-ipynb .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight-ipynb .gs { font-weight: bold } /* Generic.Strong */
.highlight-ipynb .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight-ipynb .gt { color: #0044DD } /* Generic.Traceback */
.highlight-ipynb .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight-ipynb .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight-ipynb .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight-ipynb .kp { color: #008000 } /* Keyword.Pseudo */
.highlight-ipynb .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight-ipynb .kt { color: #B00040 } /* Keyword.Type */
.highlight-ipynb .m { color: #666666 } /* Literal.Number */
.highlight-ipynb .s { color: #BA2121 } /* Literal.String */
.highlight-ipynb .na { color: #7D9029 } /* Name.Attribute */
.highlight-ipynb .nb { color: #008000 } /* Name.Builtin */
.highlight-ipynb .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight-ipynb .no { color: #880000 } /* Name.Constant */
.highlight-ipynb .nd { color: #AA22FF } /* Name.Decorator */
.highlight-ipynb .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight-ipynb .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight-ipynb .nf { color: #0000FF } /* Name.Function */
.highlight-ipynb .nl { color: #A0A000 } /* Name.Label */
.highlight-ipynb .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight-ipynb .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight-ipynb .nv { color: #19177C } /* Name.Variable */
.highlight-ipynb .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight-ipynb .w { color: #bbbbbb } /* Text.Whitespace */
.highlight-ipynb .mb { color: #666666 } /* Literal.Number.Bin */
.highlight-ipynb .mf { color: #666666 } /* Literal.Number.Float */
.highlight-ipynb .mh { color: #666666 } /* Literal.Number.Hex */
.highlight-ipynb .mi { color: #666666 } /* Literal.Number.Integer */
.highlight-ipynb .mo { color: #666666 } /* Literal.Number.Oct */
.highlight-ipynb .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight-ipynb .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight-ipynb .sc { color: #BA2121 } /* Literal.String.Char */
.highlight-ipynb .dl { color: #BA2121 } /* Literal.String.Delimiter */
.highlight-ipynb .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight-ipynb .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight-ipynb .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight-ipynb .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight-ipynb .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight-ipynb .sx { color: #008000 } /* Literal.String.Other */
.highlight-ipynb .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight-ipynb .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight-ipynb .ss { color: #19177C } /* Literal.String.Symbol */
.highlight-ipynb .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight-ipynb .fm { color: #0000FF } /* Name.Function.Magic */
.highlight-ipynb .vc { color: #19177C } /* Name.Variable.Class */
.highlight-ipynb .vg { color: #19177C } /* Name.Variable.Global */
.highlight-ipynb .vi { color: #19177C } /* Name.Variable.Instance */
.highlight-ipynb .vm { color: #19177C } /* Name.Variable.Magic */
.highlight-ipynb .il { color: #666666 } /* Literal.Number.Integer.Long */</style>
<style type="text/css">
/* Temporary definitions which will become obsolete with Notebook release 5.0 */
.ansi-black-fg { color: #3E424D; }
.ansi-black-bg { background-color: #3E424D; }
.ansi-black-intense-fg { color: #282C36; }
.ansi-black-intense-bg { background-color: #282C36; }
.ansi-red-fg { color: #E75C58; }
.ansi-red-bg { background-color: #E75C58; }
.ansi-red-intense-fg { color: #B22B31; }
.ansi-red-intense-bg { background-color: #B22B31; }
.ansi-green-fg { color: #00A250; }
.ansi-green-bg { background-color: #00A250; }
.ansi-green-intense-fg { color: #007427; }
.ansi-green-intense-bg { background-color: #007427; }
.ansi-yellow-fg { color: #DDB62B; }
.ansi-yellow-bg { background-color: #DDB62B; }
.ansi-yellow-intense-fg { color: #B27D12; }
.ansi-yellow-intense-bg { background-color: #B27D12; }
.ansi-blue-fg { color: #208FFB; }
.ansi-blue-bg { background-color: #208FFB; }
.ansi-blue-intense-fg { color: #0065CA; }
.ansi-blue-intense-bg { background-color: #0065CA; }
.ansi-magenta-fg { color: #D160C4; }
.ansi-magenta-bg { background-color: #D160C4; }
.ansi-magenta-intense-fg { color: #A03196; }
.ansi-magenta-intense-bg { background-color: #A03196; }
.ansi-cyan-fg { color: #60C6C8; }
.ansi-cyan-bg { background-color: #60C6C8; }
.ansi-cyan-intense-fg { color: #258F8F; }
.ansi-cyan-intense-bg { background-color: #258F8F; }
.ansi-white-fg { color: #C5C1B4; }
.ansi-white-bg { background-color: #C5C1B4; }
.ansi-white-intense-fg { color: #A1A6B2; }
.ansi-white-intense-bg { background-color: #A1A6B2; }

.ansi-bold { font-weight: bold; }
</style><script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<style type="text/css">
</style>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Lately I've been playing around with the <a href="https://trilinos.org/packages/anasazi/">anasazi</a> library. It's basically a library that implements algorithms to solve eigenvalue problems that are all completely unaware of the underling data structures. The way this is done is by implementing the algorithms in terms of an <strong>interface</strong>. Basically, this interface is a contract between whoever wrote the library, and whoever is using it. It's a formal way for the library writer to say "If you give me an object that implements x, and y, this library will do Z with that object."</p>
<p>This idea is a bit... abstract. <em>And that's the whole point</em>. Two places where this idea is used constantly are the Python Standard Library and the C++ Standard Template Library (STL). In Python, any object that implements __iter<strong> and \</strong>next__ is automatically considered an iterable, and this opens up a ton of the standard library. In C++, similar functionality is done using iterators, the basic type that all of the STL algorithms work on.</p>
<p>In python, for instance, this allows you to define a custom collection with __iter<strong> and \</strong>next__, and now you automatically get any(), all(), list() and so on, <em>regardless of what it is your collection does</em>.</p>
<p>This has the significant advantage that the algorithms and data structures you use become decoupled. Therefore to implement N algorithms on M data structures, you only need to implement N + M things around a common interface, rather than the N * M combinations of algorithms and data structures. It's never quite this amazing in practice, but it's close.</p>
<h2 id="Moving-Past-numpy:-Separating-Algorithms-and-data-structures-in-Linear-Algebra">Moving Past numpy: Separating Algorithms and data structures in Linear Algebra<a class="anchor-link" href="#Moving-Past-numpy:-Separating-Algorithms-and-data-structures-in-Linear-Algebra">&#182;</a></h2><p>This is getting long winded. Assume for now that numpy is not doing what we need (say, we need memory - distributed matrices for our problem or something). Rather than rewrite an entire algorithm for another type, why not abstract away numpy in the first place? Then we simply need to write an interface between our algorithm and any data structure we want it to be able to use.</p>
<h2 id="Case-Study---The-Similarity-Transform">Case Study - The Similarity Transform<a class="anchor-link" href="#Case-Study---The-Similarity-Transform">&#182;</a></h2><p>Python's duck typing actually makes this almost too easy to be true. However I prefer the explicit abstract method interface: here's the imports:</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[13]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">abc</span> <span class="k">import</span> <span class="n">ABC</span><span class="p">,</span> <span class="n">ABCMeta</span><span class="p">,</span> <span class="n">abstractmethod</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="n">np</span><span class="o">.</span><span class="n">set_printoptions</span><span class="p">(</span><span class="n">suppress</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="kn">from</span> <span class="nn">IPython.display</span> <span class="k">import</span> <span class="n">display</span>
</pre></div>
    </div>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Lets write out a function for a similarity transform,
$\mathbf{\tilde{A}} = \mathbf{S}^{-1}\mathbf{A}\mathbf{S}$,
but let's use this idea of an abstract interface. The funny thing is, this looks remarkable like psuedo - code:</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[14]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">SimilarityTransform</span><span class="p">(</span><span class="n">STInterface</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span>
    <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">STInterface</span><span class="p">,</span> <span class="n">SimilarityTransformInterface</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">STInterface</span><span class="o">.</span><span class="n">inverse</span><span class="p">()</span> <span class="o">@</span> <span class="n">other</span> <span class="o">@</span> <span class="n">STInterface</span>
</pre></div>
    </div>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Here we assumed that there's something out there called a SimilarityTransformInterface, and the thing we are being passed is an instance of that. Think for a second: what would this interface need to look like? Well, anything conforming to this interface has to implement an inverse() method as well as the @ operator, the python operator for matrix multliplication (since Python 3.5 - you're not still using python 2 right?).</p>
<p>The cool thing is, you can express this idea by defining an <em>Abstract Base Class</em> with <em>Abstract Methods</em>. Basically, an abstract base class cannot be instantiated, but it can be subclassed. The rule is, any subclass must implement all methods marked as abstract by the @abstractmethod decorator.</p>
<p>So let's define our abstract base class:</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[15]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">class</span> <span class="nc">SimilarityTransformInterface</span><span class="p">(</span><span class="n">metaclass</span><span class="o">=</span><span class="n">ABCMeta</span><span class="p">):</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">inverse</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span> <span class="k">pass</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">__matmul__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span> <span class="k">pass</span>
    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">__subclasshook__</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">C</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;Any class that implements all abstract methods of this ABC is a subclass.</span>
<span class="sd">        </span>
<span class="sd">        This does not require that they inherit from this class!!!        </span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="k">if</span> <span class="bp">cls</span> <span class="ow">is</span> <span class="n">SimilarityTransformInterface</span><span class="p">:</span>
            <span class="n">requirements_met</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="vm">__class__</span><span class="o">.</span><span class="n">__abstractmethods__</span><span class="p">:</span>
                <span class="n">requirements_met</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">any</span><span class="p">(</span><span class="n">r</span> <span class="ow">in</span> <span class="n">B</span><span class="o">.</span><span class="vm">__dict__</span> <span class="k">for</span> <span class="n">B</span> <span class="ow">in</span> <span class="n">C</span><span class="o">.</span><span class="vm">__mro__</span><span class="p">))</span>
            <span class="k">if</span> <span class="nb">all</span><span class="p">(</span><span class="n">requirements_met</span><span class="p">):</span>
                <span class="k">return</span> <span class="kc">True</span>
        <span class="k">return</span> <span class="bp">NotImplemented</span>
</pre></div>
    </div>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Here we've basically instructed anybody who wants to subclass this class that they must implement inverse() and __matmul__ themselves.</p>
<p>But that's not all. The __subclasshoook__ method is where it gets real funky. It basically patches python's issubclass and isinstance methods, and this function as written here basically tells python that  <strong>any class that implements all of the abstractmethods IS A SimilarityTransformInterface</strong>, and there's no need to inherit from it!</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[36]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">class</span> <span class="nc">NotOne</span><span class="p">:</span> <span class="k">pass</span>
<span class="k">class</span> <span class="nc">IsOne</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">inverse</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span> <span class="k">pass</span>
    <span class="k">def</span> <span class="nf">__matmul__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span> <span class="k">pass</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">issubclass</span><span class="p">(</span><span class="n">NotOne</span><span class="p">,</span> <span class="n">SimilarityTransformInterface</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">issubclass</span><span class="p">(</span><span class="n">IsOne</span><span class="p">,</span> <span class="n">SimilarityTransformInterface</span><span class="p">))</span>
</pre></div>
    </div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">
    <div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>False
True
</pre>
</div>
</div>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>So now we've defined our interface, and we can check to make sure whatever we're being passed conforms to it. We're now officially done writing the algorithm. Now all we have to do is write a wrapper for whatever our data types are to make them conform to the interface. I did this for numpy arrays below by copying fromt their documentation:</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[16]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">class</span> <span class="nc">NumpyShim</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">ndarray</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;This wraps a numpy array object into a SimiliarityTransformInterface compliant object.&quot;&quot;&quot;</span>
    <span class="k">def</span> <span class="nf">__new__</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">input_array</span><span class="p">):</span>
        <span class="n">obj</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">asarray</span><span class="p">(</span><span class="n">input_array</span><span class="p">)</span><span class="o">.</span><span class="n">view</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">obj</span>
    <span class="k">def</span> <span class="nf">__array_finalize__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">obj</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span> <span class="k">return</span>
    <span class="k">def</span> <span class="nf">inverse</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;I just used the np.linalg.inv inverse&quot;</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">linalg</span><span class="o">.</span><span class="n">inv</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</pre></div>
    </div>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Ignore the __new<strong> and \</strong>aray_finalize<strong> functions. They have to do with complications of subclassing numpy arrays. Since numpy already defines the \</strong>matmul__ function (for using @ on numpy arrays) all I have to define is the inverse. Numpy also has an inverse function, so I can just call that function within inverse(). Right now this all probably looks like a lot more work to write a one line numpy function, but bear with me.</p>
<p>Let's first make sure that our similarity transform algorithm works on numpy arrays. We can test this by diagonalizing a symmetric matrix, and seeing if we can use the eigenvectors to transform it into a diagonal matrix of eigenvalues.</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[37]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">A</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randn</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="mi">4</span><span class="p">)</span>
<span class="n">A</span> <span class="o">=</span> <span class="n">A</span> <span class="o">+</span> <span class="n">A</span><span class="o">.</span><span class="n">T</span>
<span class="n">evals</span><span class="p">,</span> <span class="n">evecs</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linalg</span><span class="o">.</span><span class="n">eigh</span><span class="p">(</span><span class="n">A</span><span class="p">)</span>
<span class="n">S</span> <span class="o">=</span> <span class="n">NumpyShim</span><span class="p">(</span><span class="n">evecs</span><span class="p">)</span>
<span class="n">M</span> <span class="o">=</span> <span class="n">NumpyShim</span><span class="p">(</span><span class="n">A</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Eigenvalues are: &quot;</span><span class="p">,</span> <span class="n">evals</span><span class="p">)</span>
<span class="n">SimilarityTransform</span><span class="p">(</span><span class="n">S</span><span class="p">,</span> <span class="n">M</span><span class="p">)</span>
</pre></div>
    </div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">
    <div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>Eigenvalues are:  [-3.71087275 -1.94249831 -0.09555686  3.90007723]
I just used the np.linalg.inv inverse
</pre>
</div>
</div>
<div class="output_area">
    <div class="prompt output_prompt">Out[37]:</div>
<div class="output_text output_subarea output_execute_result">
<pre>NumpyShim([[-3.71087275, -0.        , -0.        ,  0.        ],
           [-0.        , -1.94249831, -0.        ,  0.        ],
           [ 0.        ,  0.        , -0.09555686, -0.        ],
           [ 0.        ,  0.        , -0.        ,  3.90007723]])</pre>
</div>
</div>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Wohoo! It works! But that was a lot of work for basically nothing. Here's where it can get interesting. We know that we have orthogonal eigenvectors of a hermitian matrix, and we know that the inverse of an orthogonal matrix is just it's transpose. So let's not waste our time calculating the inverse when we could just do the transpose. But we don't wanna mess with the algorithm when we know it works:</p>
<p>Let's do this by making a specialized OrthogonalArray class, whose inverse() method is just the transpose operation. Like so:</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[28]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">class</span> <span class="nc">OrthogonalArray</span><span class="p">(</span><span class="n">NumpyShim</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Specializes inverse function for orthogonal numpy arrays&quot;&quot;&quot;</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
        <span class="k">assert</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">allclose</span><span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">T</span> <span class="o">@</span> <span class="bp">self</span> <span class="o">-</span> <span class="n">np</span><span class="o">.</span><span class="n">eye</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="p">))),</span> <span class="mf">0.0</span> <span class="p">)),</span> <span class="s2">&quot;Must be orthogonal!&quot;</span>
    <span class="k">def</span> <span class="nf">inverse</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;I just used the orthogonal array inverse&quot;</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">T</span>
</pre></div>
    </div>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Now all we have to do is convert our eigenvectors to be an OrthogonalArray and call the similarity transform on that. Note that it uses the orthogonal array inverse function.</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[38]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sym</span> <span class="o">=</span> <span class="n">OrthogonalArray</span><span class="p">(</span><span class="n">evecs</span><span class="p">)</span>
<span class="n">SimilarityTransform</span><span class="p">(</span><span class="n">sym</span><span class="p">,</span> <span class="n">A</span><span class="p">)</span>
</pre></div>
    </div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">
    <div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>I just used the orthogonal array inverse
</pre>
</div>
</div>
<div class="output_area">
    <div class="prompt output_prompt">Out[38]:</div>
<div class="output_text output_subarea output_execute_result">
<pre>OrthogonalArray([[-3.71087275, -0.        , -0.        ,  0.        ],
                 [-0.        , -1.94249831,  0.        ,  0.        ],
                 [-0.        , -0.        , -0.09555686, -0.        ],
                 [ 0.        ,  0.        , -0.        ,  3.90007723]])</pre>
</div>
</div>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Ok that's pretty neat, isn't it? We can specialize our data structures to optimize certain restrictions that we know to be true. But the underlying algorithm is unchanged.</p>
<p>If you're still not convinced, imagine the following: You could use a sparse array, an out-of-memory dask array, or maybe a massively parallel Trilinos or Petsc array to do this <strong>same algorithm</strong> they just <em>need to implement the correct interface</em>.</p>
<h2 id="Ok-let's-get-real-weird">Ok let's get real weird<a class="anchor-link" href="#Ok-let's-get-real-weird">&#182;</a></h2><p>Allow me to demonstrate. I'm going to use the same function to do a <em>symbolic</em> similarity transform using sympy.</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[30]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sympy</span> <span class="k">import</span> <span class="n">Matrix</span><span class="p">,</span> <span class="n">init_printing</span><span class="p">,</span> <span class="n">symbols</span>
<span class="n">init_printing</span><span class="p">(</span><span class="n">use_unicode</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="k">class</span> <span class="nc">SympyShim</span><span class="p">(</span><span class="n">Matrix</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">mat</span><span class="p">):</span>
        <span class="bp">self</span> <span class="o">=</span> <span class="n">mat</span>
    <span class="k">def</span> <span class="nf">inverse</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">inv</span><span class="p">()</span>
</pre></div>
    </div>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Again, sympy implements the @ operator for us already. (We could have actually required .inv() instead of .inverse() and used both numpy and sympy, but I wanted to illustrate). So we spend the 10 seconds it takes to implement our interface using sympy Matrices.</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[31]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">a</span><span class="p">,</span> <span class="n">b</span> <span class="o">=</span> <span class="n">symbols</span><span class="p">(</span><span class="s1">&#39;a b&#39;</span><span class="p">)</span>
<span class="n">a</span> <span class="o">=</span> <span class="n">Matrix</span><span class="p">([[</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">],</span> <span class="p">[</span><span class="n">b</span><span class="p">,</span> <span class="n">a</span><span class="p">]])</span>
<span class="n">display</span><span class="p">(</span><span class="n">a</span><span class="p">)</span>
</pre></div>
    </div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">
    <div class="prompt"></div>
<div class="output_latex output_subarea ">
$$\left[\begin{matrix}a & b\\b & a\end{matrix}\right]$$
</div>
</div>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Let's take a look at the eigenvalues and vectors:</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">pair1</span><span class="p">,</span> <span class="n">pair2</span> <span class="o">=</span> <span class="n">a</span><span class="o">.</span><span class="n">eigenvects</span><span class="p">()</span>
<span class="n">display</span><span class="p">(</span><span class="n">pair1</span><span class="p">)</span>
<span class="n">display</span><span class="p">(</span><span class="n">pair2</span><span class="p">)</span>
</pre></div>
    </div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">
    <div class="prompt"></div>
<div class="output_latex output_subarea ">
$$\left ( a - b, \quad 1, \quad \left [ \left[\begin{matrix}-1\\1\end{matrix}\right]\right ]\right )$$
</div>
</div>
<div class="output_area">
    <div class="prompt"></div>
<div class="output_latex output_subarea ">
$$\left ( a + b, \quad 1, \quad \left [ \left[\begin{matrix}1\\1\end{matrix}\right]\right ]\right )$$
</div>
</div>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Sympy gives us (eigenvalue, multiplicity, eigenvector) tuples as a result, so we have our eigenvectors and values. Lets make a single matrix for the vectors:</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sympy_evecs</span> <span class="o">=</span> <span class="n">pair1</span><span class="p">[</span><span class="mi">2</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">col_insert</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">pair2</span><span class="p">[</span><span class="mi">2</span><span class="p">][</span><span class="mi">0</span><span class="p">])</span>
<span class="n">sympy_evecs</span>
</pre></div>
    </div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">
    <div class="prompt output_prompt">Out[11]:</div>
<div class="output_latex output_subarea output_execute_result">
$$\left[\begin{matrix}-1 & 1\\1 & 1\end{matrix}\right]$$
</div>
</div>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Now just convert to our interface type, and use our similarity transform:</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">s</span> <span class="o">=</span> <span class="n">SympyShim</span><span class="p">(</span><span class="n">sympy_evecs</span><span class="p">)</span>
<span class="n">SimilarityTransform</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="n">a</span><span class="p">)</span>
</pre></div>
    </div>
</div>
</div>
<div class="output_wrapper">
<div class="output">
<div class="output_area">
    <div class="prompt output_prompt">Out[12]:</div>
<div class="output_latex output_subarea output_execute_result">
$$\left[\begin{matrix}a - b & 0\\0 & a + b\end{matrix}\right]$$
</div>
</div>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><strong>What the &gt;^_!</strong> it works!!!  Ok maybe I'm overexaggerating what's going on here but I've demonstrated the core idea here. This is an incredibly simple function that I'm implementing but the core idea is the same. <strong>The duck typing of Python makes it an ideal language to implement abstract algorithms that are independent of the underling datatypes</strong>. Can you do this type of thing in C++? Surely, but get your templates and 1200 character types ready.</p>
<p>I also think that a lot of linear algebra algorithms are a great target for this approach. Writing a lot of the interface code is quite straightforward (it really really really looks like pseudo code) and then you just have to wrap a lot of very commonly implemented tasks anyway (inverse, dot product, etc).</p>
<p>Then you can leverage a lot of linear algebra packages: numpy/scipy, theano, dask, pestc, trilinos, CUDABLAS, tensorflow, etc. with the same algorithms.</p>
<p>You can also do <strong>Matrix free computation where you never even store a matrix</strong>. This problem happens all the time if you're dealing with very large matrices that are hundreds of thousands or millions of rows.</p>
<p>Maybe we can re implement <a href="https://trilinos.org/packages/anasazi/">anasazi</a> eigensolvers at the algorithm level in python. Then we can have plug-n-play Lanczos, Arnoldi, Davidson, etc algorithms.</p>
<p>Last thing then I'll be quiet. Imagine using this approach in conjunction with numpy as a proof of concept of your algorithm. Come production time, just write a wrapper for theano and if you do it properly you ought to be able to generate the compute graph of your entire algorithm, and let theano optimize and compile it. I really think this approach to solving problems will really shine when paired with the Python scientific stack.</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span>
</pre></div>
    </div>
</div>
</div>
</div>
<script type="text/javascript">if (!document.getElementById("mathjaxscript_pelican_#%@#$@#")) {
    var mathjaxscript = document.createElement("script");
    mathjaxscript.id = "mathjaxscript_pelican_#%@#$@#";
    mathjaxscript.type = "text/javascript";
    mathjaxscript.src = "//cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML";
    mathjaxscript[(window.opera ? "innerHTML" : "text")] =
        "MathJax.Hub.Config({" +
        "    config: ['MMLorHTML.js']," +
        "    TeX: { extensions: ['AMSmath.js', 'AMSsymbols.js', 'noErrors.js', 'noUndefined.js'], equationNumbers: { autoNumber: 'AMS' } }," +
        "    jax: ['input/TeX', 'input/MathML', 'output/HTML-CSS']," +
        "    extensions: ['tex2jax.js', 'mml2jax.js', 'MathMenu.js', 'MathZoom.js']," +
        "    displayAlign: 'center'," +
        "    displayIndent: '0em'," +
        "    showMathMenu: true," +
        "    tex2jax: { " +
        "        inlineMath: [ ['$', '$'] ], " +
        "        displayMath: [ ['$$', '$$'] ]," +
        "        processEscapes: true," +
        "        preview: 'TeX'," +
        "    }, " +
        "    'HTML-CSS': { " +
        " linebreaks: { automatic: true, width: '95% container' }, " +
        "        styles: { '.MathJax_Display, .MathJax .mo, .MathJax .mi, .MathJax .mn': {color: 'black ! important'} }" +
        "    } " +
        "}); ";
    (document.body || document.getElementsByTagName("head")[0]).appendChild(mathjaxscript);
}
</script>

</div>
