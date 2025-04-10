using System;

class Student
{
    public string Name { get; set; }
    public int ID { get; set; }
    public int Marks { get; set; }

    // Constructor
    public Student(string name, int id, int marks)
    {
        Name = name;
        ID = id;
        Marks = marks;
    }

    // Method to determine grade
    public string GetGrade()
    {
        if (Marks >= 90) return "A";
        if (Marks >= 80) return "B";
        if (Marks >= 70) return "C";
        return "D";
    }
}

class StudentIITGN : Student
{
    public string Hostel_Name_IITGN { get; set; }

    // Constructor calling base class constructor
    public StudentIITGN(string name, int id, int marks, string hostelName)
        : base(name, id, marks)
    {
        Hostel_Name_IITGN = hostelName;
    }

    // Display IITGN student details
    public new void DisplayDetails()
    {
        Console.WriteLine($"Name: {Name}");
        Console.WriteLine($"ID: {ID}");
        Console.WriteLine($"Marks: {Marks}");
        Console.WriteLine($"Grade: {GetGrade()}");
        Console.WriteLine($"Hostel: {Hostel_Name_IITGN}");
    }
}

class Program
{
    static void Main()
    {
        // Creating student object
        Student student1 = new Student("John", 12345, 85);
        Console.WriteLine("Student Details:");
        Console.WriteLine($"Name: {student1.Name}");
        Console.WriteLine($"ID: {student1.ID}");
        Console.WriteLine($"Marks: {student1.Marks}");
        Console.WriteLine($"Grade: {student1.GetGrade()}");

        // Creating IITGN student object
        StudentIITGN studentIITGN = new StudentIITGN("Alice", 67890, 92, "Hostel 2");
        Console.WriteLine("\nIITGN Student Details:");
        studentIITGN.DisplayDetails();
    }
}
