from handle_command_line import handle_command_line, log_command_line_structure
import sys

def main():
    if len(sys.argv) in [4, 6]:
        handle_command_line(sys.argv)
    else: 
        log_command_line_structure()
        
        return 1    
    
    return 0
    
        
if __name__ == "__main__":
    main()
