use inputbot::KeySequence;
use std::io::{self, Write};

fn main() {
    let mut count = 0;
    while count < 3 {
        print!("请将光标置于需要输入的位置，{} 秒后开始输入", 3 - count);
        io::stdout().flush().unwrap();
        std::thread::sleep(std::time::Duration::from_secs(1));
        count += 1;
        print!("\r"); // 打印完数字后，使用\r回到行首
    }

    let args: Vec<String> = std::env::args().skip(1).collect();
    let joined_args = args.join(" ");
    let arg_str: &'static str = Box::leak(joined_args.into_boxed_str());

    KeySequence(arg_str).send();
    println!("\n输入完成");
}
