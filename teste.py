import js2py

js="""function add(x,y){
    return x+y
}
const sum=add(3,12);
"""
a=int(input("enter a number : "))
context=js2py.EvalJs()
context.execute(js)
b=context.sum
c=a+b
print(c)

# js="""function scraper(driver, tr){
#             let css_before = window.getComputedStyle(table.cards td, '::before')
#             td = css_before.content
#             return td
#         }
#         const td=scraper(driver, tr)"""
#         context=js2py.EvalJs()
#         context.execute(js)
#         b=context.td
#         print(b)