import { Component, OnInit } from '@angular/core';
import { AlbumsService } from '../api/albums.service';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage implements OnInit {
  albums = []; /* [
    {
      titulo_album: "crush",
      ano_produccion: "2000",
      nombre_artista: "bon jovi",
      tracks: "it is my life",
      link_caratula: "https://www.guitarraviva.com/wp-content/uploads/2016/09/bon-jovi-its-my-life.jpg",
    }
  ];*/

  constructor(private albumsService: AlbumsService) {}

  ngOnInit(){
    this.albumsService.albums.subscribe(albums => {
      this.albums = albums;
    });
    //this.albumsService.getAlbums();
  }

}
