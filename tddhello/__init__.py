import check50
import check50_java

@check50.check()
def exists():
    """Hello.java exists"""
    check50.exists("Hello.java")

@check50.check(exists)
def hello_compiles():
    """Hello.java compiles"""
    check50_java.compile ("Hello.java")

@check50.check(hello_compiles)    
def hello_main_exists():
    """Hello is application """
    check50_java.checks.is_application_class("Hello")    

@check50.check(hello_main_exists)
def hello_main_output():
    """Hello.main() output"""
    expected = "hello world\n"
    actual = check50_java.run("Hello").stdout()
    help_msg = "did you introduce a trailing newline or whitespace characters?"
    if actual != expected:
        raise check50.Mismatch(expected, actual, help=help_msg)


