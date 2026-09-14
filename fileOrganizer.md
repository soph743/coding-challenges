### requirements:

in bash or python, create a tool that, given a top-level folder, recursively searches the folder and returns statistics on the file type in the format:

```jsx
<top-level folder name> statistics
		/<folder 1 name>
			videos: ..
			images: ..
			text: ..
			data (CSV, excel): ..
			models (.pt, .yaml, .pth, .h5, etc): ..
			other: ..
			/<folder 1A name>
				...
		/<folder 2 name>
		...
```

the program should support a single flag `--summary` which, if passed, returns the summarized statistics for contained files and subfolders:

```jsx
<top-level folder name> summary statistics
	videos: ..
	images: ..
	text: ..
	data (CSV, excel): ..
	models (.pt, .yaml, .pth, .h5, etc): ..
	other: ..
```
