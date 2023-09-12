void setup() {
  // put your setup code here, to run once:
  pinMode(8, OUTPUT);
  Serial.begin(9600);

}
int n=0;
int listx[100];
int listy[100];

void process(int list[])
{
  while(serial.available()==0)
  {
    //Spends time while python sends anything back
  }
  while(serial.available() >0)
  {
    String inputString = Serial.readStringUntil('\n'); // Read until a newline character

    // Initialize variables
     // Assuming a maximum of 100 integers
    int count = 0;

    // Tokenize the input string
    char *token = strtok(const_cast<char*>(inputString.c_str()), " ");

    while (token != NULL) 
    {
      // Convert the token to an integer and store it in the array
      list[count] = atoi(token);
      count++;

      // Get the next token
      token = strtok(NULL, " ");
      serial.println("Y"); //Acknowledgement to python
    }
}

void loop() 
{
  // put your main code here, to run repeatedly:
  if (n==0)
  {
    process(listx);
    n=1;
  }
  if (n==1)
  {
    process(listy);
    n=0;
    //All the computation statements to move the motors using arduino
  } 
}
