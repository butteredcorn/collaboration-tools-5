#### Q1: Why are readme's in github in the .md format? What is .md and why does github use it instead of .txt, .html .docx, or any other file format?

>Markdown is good for documentation purposes. It allows plain text to be readable without tags, but still gives you functionalities like the ability to bold, italicize, change font size, declare headers, link images and urls. It also works with HTML and CSS.
>
>It also allows for programming language syntaxing which is something that a .txt, .html, .docx does not support. It even links to your GitHub repo effortlessly.


#### Q2: Is the keyword "fixes" the only way to auto-close an issue from a PR (pull request). Is there other keywords that can accomplish the same thing?

>According to [Github](https://help.github.com/en/github/managing-your-work-on-github/linking-a-pull-request-to-an-issue), they support 9 keywords: close, closes, closed, fix, fixes, fixed, resolve, resolves, resolved. All of these keywords allow you to link a pull request to an issue.

#### Q3: Do you have to create a new PR EVERYTIME you want to close an issue, or is it possible to close multiple issues within a single PR? If so, how?

>You can type something like '_fixes #1, fixes #2, fixes #3; commit message_' to link one pull request to multiple issues. 


Thanks for reading.
