budou-chart
===========

Gather burn down chart data from repository commit history.

## Usage

`python budou.py output-file.csv hours-multiplier start-at-week end-at-week`

Options:

- **output-file.csv** _(output file for data)_
- **hours-multiplier** _(increase or decrease this value to get a more accurate estimation of work hours for a particular project)_
- **start-at-week** _(get data starting from, and including, this week)_
- **end-at-week** _(get data up to, and including, this week)_

Example:

`python budou.py results.csv 0.005 1409443000 1410654000`

## Notes

See LICENSE file for license information.
