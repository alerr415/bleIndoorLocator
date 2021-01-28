using Godot;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net.Sockets;
using System.Threading;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Input;

using System.Threading;

public class Node2D : Godot.Node2D
{
	// Declare member variables here. Examples:
	// private int a = 2;
	// private string b = "text";
	int state = 0;
	Container DataSet = new Container();
	TcpClient client;
	
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
	
		try
			{
				Int32 port = 4242;
				client = new TcpClient("10.20.10.216", port);
			}
			catch (ArgumentNullException e)
			{
				Console.WriteLine("ArgumentNullException: {0}", e);
			}
			catch (SocketException e)
			{
				Console.WriteLine("SocketException: {0}", e);
			}
		}
		
		
	

//  // Called every frame. 'delta' is the elapsed time since the previous frame.
  public override void _Process(float delta)
 {
	NetworkStream stream = client.GetStream();
	Byte[] data = new Byte[256];

				// String to store the response ASCII representation.
	String responseData = String.Empty;
	System.Threading.Thread.Sleep(500);
	Int32 bytes = stream.Read(data, 0, data.Length);
	responseData = System.Text.Encoding.ASCII.GetString(data, 0, bytes);
	DataSet.Add(responseData);
	
	ColorRect iroda        = GetNode<ColorRect>("iroda");
	ColorRect ebedlo       = GetNode<ColorRect>("ebedlo");
	ColorRect mernok2      = GetNode<ColorRect>("mernok2");
	ColorRect mernok1      = GetNode<ColorRect>("mernok1");
	ColorRect kistargyalo  = GetNode<ColorRect>("kistargyalo");
	ColorRect nagytargyalo = GetNode<ColorRect>("nagytargyalo");
	bool[] van = new bool[6];
	
	foreach(Person asd in DataSet.samples){
		if(asd.location =="iroda"){       van[0]=true;}
		if(asd.location =="ebedlo"){      van[1]=true;}
		if(asd.location =="mernok2"){     van[2]=true;}
		if(asd.location =="mernok1"){     van[3]=true;}
		if(asd.location =="kistargyalo"){ van[4]=true;}
		if(asd.location =="nagytargyalo"){van[5]=true;}
		
	}
	for(int i =0;i<6;i++){
		if(van[0]==true){iroda.Color = new Color("#7CFC00");}
		else{iroda.Color = new Color("#000000");}
		
		if(van[1]==true){ebedlo.Color = new Color("#7CFC00");}
		else{ebedlo.Color = new Color("#000000");}
		
		if(van[2]==true){mernok2.Color = new Color("#7CFC00");}
		else{mernok2.Color = new Color("#000000");}
		
		if(van[3]==true){mernok1.Color = new Color("#7CFC00");}
		else{mernok1.Color = new Color("#000000");}
		
		if(van[4]==true){kistargyalo.Color = new Color("#7CFC00");}
		else{kistargyalo.Color = new Color("#000000");}
		
		if(van[5]==true){nagytargyalo.Color = new Color("#7CFC00");}
		else{nagytargyalo.Color = new Color("#000000");}
		
	}
	int[] Counter = new int[6];
	Counter = DataSet.Count();
	
	Label Labelmernok1 =  GetNode<Label>("Labelmernok1");
	Label Labelmernok2 =  GetNode<Label>("Labelmernok2");
	Label LabelIroda =  GetNode<Label>("LabelIroda");
	Label Labelnagytargyalo = GetNode<Label>("Labelnagytargyalo");
	Label Labelebedlo =  GetNode<Label>("Labelebedlo");
	Label Labelkistargyalo =  GetNode<Label>("Labelkistargyalo");
	
	LabelIroda.Text= Counter[0].ToString();
	Labelebedlo.Text= Counter[1].ToString();
	Labelmernok2.Text= Counter[2].ToString();
	Labelmernok1.Text = Counter[3].ToString();
	Labelkistargyalo.Text=Counter[4].ToString();
	Labelnagytargyalo.Text= Counter[5].ToString();

System.Threading.Thread.Sleep(1000);
					
 }

			
 public class Container
	{
	  
		
		public List<Person> samples = new List<Person>();

	  

		public void Add(string item)
		{
			bool existing = false;
			Person newdata = new Person(item);
			foreach(Person obj in samples)
			{
				if(obj.name == newdata.name){
					obj.location = newdata.location;
					existing=true;
					
				}
				
				
			}
			if(!existing){
			samples.Add(new Person(item));
			
			}
		}

		public int[] Count()
		{
			int[] RoomPeopleCount = new int[6];
			foreach(Person obj in samples)
			{
			switch(obj.location) 
			{
				case "iroda":
					RoomPeopleCount[0]++;
					break;
				case "ebedlo":
					RoomPeopleCount[1]++;
					break;
				case "mernok2":
					RoomPeopleCount[2]++;
					break;
				case "mernok1":
					RoomPeopleCount[3]++;
					break;
				case "kistargyalo":
					RoomPeopleCount[4]++;
					break;
				case "nagytargyalo":
					RoomPeopleCount[5]++;
					break;
					
				
				
				
				
			} 

			}
			
			return RoomPeopleCount;

		}
		
		
	}
	 public class Person
	{
		public string name { get; set; }
		public string location { get; set; }

		public Person(string record) 
		{
			Console.WriteLine(record);
			string[] temp = new string[2];
			temp = record.Split(',');
			this.name = temp[0];
			this.location = temp[1];


		}

	}
}
