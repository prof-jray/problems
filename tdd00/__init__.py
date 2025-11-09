import check50
import check50.java


@check50.check()
def exists():
    """Hello.java exists"""
    check50.exists("Hello.java")


@check50.check(exists)
def compiles():
    """Hello.java compiles"""
    check50.java.compile("Hello.java")


@check50.check(compiles)
def emma():
    """responds to name Emma"""
    check50.run("java ./Hello").stdin("Emma").stdout("Emma").exit()


@check50.check(compiles)
def rodrigo():
    """responds to name Rodrigo"""
    check50.run("java ./Hello").stdin("Rodrigo").stdout("Rodrigo").exit()


