#!/usr/bin/perl

my $sum=0;


while(<>)
{
    /(\w)\s(\w)/;
    if ($1 eq "A")
    {
	if ($2 eq "X") {$sum+=0+3;}
	elsif ($2 eq "Y") {$sum+=3+1;}
	elsif ($2 eq "Z") {$sum+=6+2;}
    }
    elsif ($1 eq "B")
    {
	if ($2 eq "X") {$sum+=0+1;}
	elsif ($2 eq "Y") {$sum+=3+2;}
	elsif ($2 eq "Z") {$sum+=6+3;}
    }
    elsif ($1 eq "C")
    {
	if ($2 eq "X") {$sum+=0+2;}
	elsif ($2 eq "Y") {$sum+=3+3;}
	elsif ($2 eq "Z") {$sum+=6+1;}
    }

    
}

print "$sum\n";
