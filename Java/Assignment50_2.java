import java.io.File;   
class FileInfo
{  
    public static void main(String[] args)
    {  
        File f0 = new File("Demo.txt");  
        if (f0.exists())
        {  
            System.out.println("The name of the file is: " + f0.getName());  
   
            System.out.println("The absolute path of the file is: " + f0.getAbsolutePath());     
   
            System.out.println("Is file writeable?: " + f0.canWrite());    
   
            System.out.println("Is file readable " + f0.canRead());    
   
            System.out.println("The size of the file in bytes is: " + f0.length());    
        } 
        else 
        {  
            System.out.println("The file does not exist.");  
        }  
    }  
}  