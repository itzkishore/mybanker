from flask import current_app as app
import pygal
from dbHelper import getInEx, getExpenseStats

# Generate bar chart for income/expense for the selected year
def inexTrend(username, year):
  chart = pygal.Bar(legend_at_bottom=True, show_y_labels=False, pretty_print=True, tooltip_border_radius=10)
  chart.title = "Income/Expense Trend for %s" % year
  chart.x_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  income_data = []
  expense_data = []
  inexdata = getInEx(username, year)
  if not inexdata is None:
    for row in inexdata:
      income_data.append(row[1])
      expense_data.append(row[2])
    chart.add('Income', income_data)
    chart.add('Expense', expense_data)
  else:
    chart.add('line', [])
  return chart.render_data_uri()

# Generate pie chart for expense stats for the selected year
def expenseStats(username, year):
  chart = pygal.Pie(legen_at_bottom=True)
  chart.title = "Expense stats for %s" % year
  expensedata = getExpenseStats(username, year)
  if not expensedata is None:
    for row in expensedata:
      chart.add(row[0], row[1])
  else:
    chart.add('line',[])
  return chart.render_data_uri()
