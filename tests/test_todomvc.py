from selene.support.shared import browser
from selene import have

# browser.config.hold_browser_open = True
browser.open('http://todomvc.com/examples/emberjs/')


def test_add_tasks():
    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    browser.all('#todo-list .view').should(have.size(3) and have.exact_texts('a', 'b', 'c'))


def test_do_task_toggle_completted():
    browser.all('#todo-list .ember-view .toggle')[1].click()


def test_check_completted_tasks():
    browser.all('#todo-list .completed .view').should(have.size(1) and have.exact_texts('b'))


def test_check_active_tasks():
    browser.all('#todo-list [class=ember-view] .view').should(have.size(2) and have.exact_texts('a', 'c'))
    # '[class=ember-view]' used here to match exactly "ember-view"
    # in the class name, without "completed ember-view" by used '.class=ember-view'
