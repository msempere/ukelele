![Logo](http://i.imgur.com/96592SA.png)

#### A portable and lightweight programming language for .Net/Mono platforms

This project is still under heavy development, **use on your own risk!**

The latest development version is in the **[develop](https://github.com/msempere/ukelele/tree/develop)** branch.

## Usage:
### How to compile:
```
$> make 
```
It will compile all .uk files in the current directory, generating .exe

### Execution:
```
$> mono test.exe 
```

Or if you hate make files:
```
$> ./bin/ukelele test.uk
```

## Examples:

### Loops:

#### While loop:
```
def main() void{
    auto i = 2;
    while(i>0){
        println(i);
        i = i - 1;
    }
    return();
}
```

#### Do-while loop:
```
def main() void{
    auto i = 0;
    do{
        println(i);
        i = i - 1;
    }
    while(i>0)
    return();
}
```

#### For loop:
```
def main() void{
    for(int i=0; i<3; i=i+1)
    {
        println(i);
    }
    return();
}
```

### Arrays:
```
def main() void{
    int a[5];
    int b[4][5][6];
    a[0] = 1;
    b[1][2][2] = a[0];
    print(a[1]);
    print(a[0]);
    return();
}

```

### Pattern matching:
```
def main() void{
    int a;
    a = 99;

    match a {
        1 -> {println("I am a 1");}
        2 -> {println("I am a 2");}
        _ -> {
                for(int i=0; i<5; i=i+1){
                    println("I told you!, I am not a small number !");
                }
            }
    }
    return();
}
```
More examples in test folder

## Requeriments
- ilasm
- mono


